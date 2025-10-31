#!/usr/bin/env python3
"""
FORGE Operational Calculator
Resource planning and execution metrics
"""

import math
from typing import Dict, List, Tuple, Optional
from datetime import datetime, timedelta
import json

class OperationalCalculator:
    """Calculate operational metrics and resource requirements."""
    
    def __init__(self):
        self.overhead_multiplier = 1.4  # 40% overhead on salaries
        self.efficiency_factors = {
            'junior': 0.5,
            'mid': 1.0,
            'senior': 1.5,
            'principal': 2.0
        }
    
    def calculate_burn_rate(self,
                           headcount: Dict[str, int],
                           salaries: Dict[str, float],
                           other_expenses: Dict[str, float]) -> Dict:
        """
        Calculate comprehensive burn rate.
        
        Args:
            headcount: {'role': count}
            salaries: {'role': annual_salary}
            other_expenses: {'category': monthly_cost}
            
        Returns:
            Burn rate breakdown
        """
        # Calculate people costs
        monthly_salaries = 0
        for role, count in headcount.items():
            if role in salaries:
                annual = salaries[role] * count * self.overhead_multiplier
                monthly_salaries += annual / 12
        
        # Sum other expenses
        monthly_other = sum(other_expenses.values())
        
        # Total burn
        total_burn = monthly_salaries + monthly_other
        
        return {
            'monthly_salaries': monthly_salaries,
            'monthly_other': monthly_other,
            'total_monthly_burn': total_burn,
            'annual_burn': total_burn * 12,
            'daily_burn': total_burn / 30,
            'cost_per_employee': monthly_salaries / sum(headcount.values()) if headcount else 0
        }
    
    def calculate_runway(self,
                        cash: float,
                        monthly_burn: float,
                        monthly_revenue: float = 0,
                        revenue_growth_rate: float = 0) -> Dict:
        """
        Calculate runway with growth projections.
        
        Args:
            cash: Current cash balance
            monthly_burn: Monthly burn rate
            monthly_revenue: Current monthly revenue
            revenue_growth_rate: Monthly revenue growth rate
            
        Returns:
            Runway analysis
        """
        months = 0
        remaining_cash = cash
        current_revenue = monthly_revenue
        projections = []
        
        while remaining_cash > 0 and months < 60:  # Cap at 5 years
            net_burn = monthly_burn - current_revenue
            remaining_cash -= net_burn
            
            projections.append({
                'month': months,
                'cash': remaining_cash,
                'revenue': current_revenue,
                'net_burn': net_burn
            })
            
            if net_burn <= 0:  # Default alive
                break
                
            current_revenue *= (1 + revenue_growth_rate)
            months += 1
        
        default_alive = net_burn <= 0
        
        return {
            'runway_months': months,
            'default_alive': default_alive,
            'break_even_month': months if default_alive else None,
            'cash_at_break_even': remaining_cash if default_alive else None,
            'projections': projections[:24]  # First 2 years only
        }
    
    def calculate_unit_economics(self,
                                 cac: float,
                                 ltv: float,
                                 gross_margin: float,
                                 monthly_churn: float) -> Dict:
        """
        Calculate unit economics metrics.
        
        Args:
            cac: Customer acquisition cost
            ltv: Customer lifetime value
            gross_margin: Gross margin percentage
            monthly_churn: Monthly churn rate
            
        Returns:
            Unit economics analysis
        """
        if monthly_churn > 0:
            customer_lifetime_months = 1 / monthly_churn
        else:
            customer_lifetime_months = float('inf')
        
        ltv_cac_ratio = ltv / cac if cac > 0 else float('inf')
        
        # CAC payback period
        average_revenue_per_user = ltv / customer_lifetime_months if customer_lifetime_months != float('inf') else 0
        monthly_gross_profit = average_revenue_per_user * gross_margin
        cac_payback_months = cac / monthly_gross_profit if monthly_gross_profit > 0 else float('inf')
        
        return {
            'ltv': ltv,
            'cac': cac,
            'ltv_cac_ratio': ltv_cac_ratio,
            'customer_lifetime_months': customer_lifetime_months,
            'cac_payback_months': cac_payback_months,
            'gross_margin': gross_margin,
            'monthly_churn': monthly_churn,
            'healthy': ltv_cac_ratio > 3 and cac_payback_months < 12
        }
    
    def calculate_mvp_resources(self,
                               features: List[Dict],
                               team_velocity: float = 20) -> Dict:
        """
        Calculate MVP resource requirements.
        
        Args:
            features: List of {'name': str, 'effort': int, 'impact': int}
            team_velocity: Story points per sprint
            
        Returns:
            MVP planning analysis
        """
        # Sort by impact/effort ratio
        for feature in features:
            feature['roi'] = feature['impact'] / feature['effort'] if feature['effort'] > 0 else 0
        
        features_sorted = sorted(features, key=lambda x: x['roi'], reverse=True)
        
        # Calculate MVP (top 20% of features)
        mvp_count = max(1, len(features) // 5)
        mvp_features = features_sorted[:mvp_count]
        
        mvp_effort = sum(f['effort'] for f in mvp_features)
        total_effort = sum(f['effort'] for f in features)
        
        mvp_sprints = math.ceil(mvp_effort / team_velocity)
        total_sprints = math.ceil(total_effort / team_velocity)
        
        return {
            'mvp_features': [f['name'] for f in mvp_features],
            'mvp_effort_points': mvp_effort,
            'mvp_sprints': mvp_sprints,
            'mvp_weeks': mvp_sprints * 2,
            'full_effort_points': total_effort,
            'full_sprints': total_sprints,
            'effort_saved': (total_effort - mvp_effort) / total_effort,
            'features_cut': len(features) - len(mvp_features)
        }
    
    def calculate_hiring_plan(self,
                            current_headcount: int,
                            target_headcount: int,
                            monthly_attrition: float = 0.01,
                            ramp_weeks: int = 12) -> Dict:
        """
        Calculate realistic hiring timeline.
        
        Args:
            current_headcount: Current team size
            target_headcount: Target team size
            monthly_attrition: Monthly attrition rate
            ramp_weeks: Weeks to full productivity
            
        Returns:
            Hiring plan analysis
        """
        months_to_target = 0
        current = current_headcount
        hires_needed = target_headcount - current_headcount
        total_hires = 0
        timeline = []
        
        # Hiring capacity constraints
        max_monthly_hires = max(1, current * 0.2)  # Can hire 20% of team per month
        
        while current < target_headcount and months_to_target < 24:
            # Calculate attrition
            attrition = current * monthly_attrition
            
            # Calculate hires (constrained by capacity)
            monthly_hires = min(max_monthly_hires, target_headcount - current + attrition)
            
            # Update headcount
            current = current - attrition + monthly_hires
            total_hires += monthly_hires
            
            timeline.append({
                'month': months_to_target,
                'headcount': round(current),
                'hires': round(monthly_hires),
                'attrition': round(attrition)
            })
            
            months_to_target += 1
            
            # Update hiring capacity
            max_monthly_hires = max(1, current * 0.2)
        
        # Account for ramp time
        productive_capacity_timeline = []
        for i, month_data in enumerate(timeline):
            ramping = sum(t['hires'] for t in timeline[max(0, i-3):i+1])
            productive = month_data['headcount'] - ramping * 0.5
            productive_capacity_timeline.append({
                'month': i,
                'total_headcount': month_data['headcount'],
                'productive_capacity': round(productive)
            })
        
        return {
            'months_to_target': months_to_target,
            'total_hires_needed': round(total_hires),
            'replacement_hires': round(total_hires - hires_needed),
            'timeline': timeline[:12],  # First year only
            'productive_capacity': productive_capacity_timeline[:12],
            'achievable': months_to_target < 24
        }
    
    def calculate_critical_path(self,
                               tasks: List[Dict]) -> Dict:
        """
        Calculate critical path for project.
        
        Args:
            tasks: List of {'name': str, 'duration': int, 'dependencies': List[str]}
            
        Returns:
            Critical path analysis
        """
        # Build task graph
        task_map = {task['name']: task for task in tasks}
        
        # Calculate early start/finish
        for task in tasks:
            task['early_start'] = 0
            task['early_finish'] = task['duration']
        
        # Forward pass
        changed = True
        while changed:
            changed = False
            for task in tasks:
                if task['dependencies']:
                    max_finish = max(
                        task_map[dep]['early_finish'] 
                        for dep in task['dependencies'] 
                        if dep in task_map
                    )
                    if task['early_start'] < max_finish:
                        task['early_start'] = max_finish
                        task['early_finish'] = max_finish + task['duration']
                        changed = True
        
        # Find project duration
        project_duration = max(task['early_finish'] for task in tasks)
        
        # Backward pass
        for task in tasks:
            task['late_finish'] = project_duration
            task['late_start'] = project_duration - task['duration']
        
        # Find critical path
        critical_tasks = []
        for task in tasks:
            task['slack'] = task['late_start'] - task['early_start']
            if task['slack'] == 0:
                critical_tasks.append(task['name'])
        
        return {
            'project_duration': project_duration,
            'critical_path': critical_tasks,
            'critical_path_length': len(critical_tasks),
            'tasks_with_slack': [t['name'] for t in tasks if t['slack'] > 0],
            'average_slack': sum(t['slack'] for t in tasks) / len(tasks) if tasks else 0
        }
    
    def calculate_build_vs_buy(self,
                              build_cost: float,
                              build_time_months: int,
                              buy_cost_monthly: float,
                              integration_cost: float) -> Dict:
        """
        Analyze build versus buy decision.
        
        Args:
            build_cost: Total cost to build
            build_time_months: Time to build
            buy_cost_monthly: Monthly subscription cost
            integration_cost: One-time integration cost
            
        Returns:
            Build vs buy analysis
        """
        # 3-year total cost comparison
        months = 36
        
        # Build option
        build_total = build_cost
        build_maintenance = build_cost * 0.2 / 12  # 20% annual maintenance
        build_total_3y = build_cost + (build_maintenance * months)
        
        # Buy option
        buy_total_3y = integration_cost + (buy_cost_monthly * months)
        
        # Break-even analysis
        if buy_cost_monthly > 0:
            break_even_months = (build_cost - integration_cost) / buy_cost_monthly
        else:
            break_even_months = float('inf')
        
        # Opportunity cost of delayed launch
        opportunity_cost = build_time_months * buy_cost_monthly * 10  # Rough estimate
        
        return {
            'build_cost_3y': build_total_3y,
            'buy_cost_3y': buy_total_3y,
            'break_even_months': break_even_months,
            'recommendation': 'buy' if buy_total_3y < build_total_3y else 'build',
            'savings_3y': abs(build_total_3y - buy_total_3y),
            'build_time_months': build_time_months,
            'opportunity_cost': opportunity_cost
        }


def main():
    """Example usage of operational calculator."""
    calc = OperationalCalculator()
    
    print("=== Startup Operational Analysis ===\n")
    
    # Burn rate calculation
    headcount = {
        'engineer': 5,
        'sales': 2,
        'ops': 1
    }
    
    salaries = {
        'engineer': 150000,
        'sales': 120000,
        'ops': 80000
    }
    
    other_expenses = {
        'office': 10000,
        'tools': 5000,
        'marketing': 15000,
        'misc': 5000
    }
    
    burn = calc.calculate_burn_rate(headcount, salaries, other_expenses)
    print(f"Monthly burn rate: ${burn['total_monthly_burn']:,.0f}")
    print(f"  Salaries: ${burn['monthly_salaries']:,.0f}")
    print(f"  Other: ${burn['monthly_other']:,.0f}\n")
    
    # Runway calculation
    cash = 2000000  # $2M in bank
    revenue = 20000  # $20K MRR
    growth = 0.15    # 15% monthly growth
    
    runway = calc.calculate_runway(cash, burn['total_monthly_burn'], revenue, growth)
    print(f"Runway Analysis:")
    print(f"  Months of runway: {runway['runway_months']}")
    print(f"  Default alive: {runway['default_alive']}")
    if runway['break_even_month']:
        print(f"  Break-even month: {runway['break_even_month']}\n")
    else:
        print(f"  Break-even: Not reached\n")
    
    # Unit economics
    unit_econ = calc.calculate_unit_economics(
        cac=1000,
        ltv=5000,
        gross_margin=0.8,
        monthly_churn=0.05
    )
    print(f"Unit Economics:")
    print(f"  LTV/CAC ratio: {unit_econ['ltv_cac_ratio']:.1f}")
    print(f"  CAC payback: {unit_econ['cac_payback_months']:.1f} months")
    print(f"  Healthy: {unit_econ['healthy']}\n")
    
    # MVP planning
    features = [
        {'name': 'Core Auth', 'effort': 5, 'impact': 10},
        {'name': 'Dashboard', 'effort': 8, 'impact': 8},
        {'name': 'API', 'effort': 13, 'impact': 9},
        {'name': 'Mobile App', 'effort': 21, 'impact': 5},
        {'name': 'Analytics', 'effort': 8, 'impact': 6},
        {'name': 'Integrations', 'effort': 13, 'impact': 7}
    ]
    
    mvp = calc.calculate_mvp_resources(features)
    print(f"MVP Analysis:")
    print(f"  MVP features: {', '.join(mvp['mvp_features'])}")
    print(f"  MVP timeline: {mvp['mvp_weeks']} weeks")
    print(f"  Effort saved: {mvp['effort_saved']:.0%}\n")
    
    # Hiring plan
    hiring = calc.calculate_hiring_plan(
        current_headcount=8,
        target_headcount=25
    )
    print(f"Hiring Plan:")
    print(f"  Months to target: {hiring['months_to_target']}")
    print(f"  Total hires needed: {hiring['total_hires_needed']}")
    print(f"  Including replacements: {hiring['replacement_hires']}")


if __name__ == "__main__":
    main()