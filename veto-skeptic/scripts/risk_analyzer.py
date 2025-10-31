#!/usr/bin/env python3
"""
VETO Risk Analysis Calculator
Quantitative tools for skeptical analysis
"""

import numpy as np
from typing import Dict, List, Tuple, Optional
import json

class RiskAnalyzer:
    """Calculate failure probabilities and risk metrics."""
    
    def __init__(self, confidence_level: float = 0.95):
        self.confidence_level = confidence_level
        self.base_rates = {
            'startup_unicorn': 0.00006,
            'new_product_success': 0.05,
            'it_project_on_time': 0.16,
            'ma_value_creation': 0.30,
            'platform_network_effects': 0.01,
            'behavior_change_scale': 0.08,
            'regulatory_approval_new': 0.22,
            'disruption_incumbent': 0.03
        }
    
    def calculate_joint_probability(self, 
                                   probabilities: List[float], 
                                   independent: bool = True) -> float:
        """
        Calculate probability of all events occurring.
        
        Args:
            probabilities: List of individual probabilities
            independent: Whether events are independent
            
        Returns:
            Joint probability
        """
        if independent:
            return np.prod(probabilities)
        else:
            # Conservative estimate for dependent events
            return np.prod(probabilities) * 0.7
    
    def monte_carlo_simulation(self,
                              base_case: float,
                              volatility: float = 0.3,
                              n_simulations: int = 10000,
                              include_black_swan: bool = True) -> Dict:
        """
        Run Monte Carlo simulation with fat-tail events.
        
        Args:
            base_case: Expected value
            volatility: Standard deviation as fraction of base
            n_simulations: Number of iterations
            include_black_swan: Include 1% catastrophic events
            
        Returns:
            Dictionary with percentiles and statistics
        """
        # Generate normal distribution
        simulations = np.random.normal(base_case, base_case * volatility, n_simulations)
        
        # Add black swan events (1% chance of -90% outcome)
        if include_black_swan:
            black_swan_mask = np.random.random(n_simulations) < 0.01
            simulations[black_swan_mask] = base_case * 0.1
        
        # Calculate percentiles
        percentiles = np.percentile(simulations, [5, 10, 25, 50, 75, 90, 95])
        
        return {
            'mean': np.mean(simulations),
            'median': np.median(simulations),
            'std': np.std(simulations),
            'p5': percentiles[0],
            'p10': percentiles[1],
            'p25': percentiles[2],
            'p50': percentiles[3],
            'p75': percentiles[4],
            'p90': percentiles[5],
            'p95': percentiles[6],
            'worst_case': np.min(simulations),
            'best_case': np.max(simulations),
            'probability_loss': np.sum(simulations < 0) / n_simulations,
            'value_at_risk_95': percentiles[0],
            'conditional_var_95': np.mean(simulations[simulations <= percentiles[0]])
        }
    
    def failure_mode_analysis(self, 
                             failure_modes: Dict[str, Tuple[float, float]]) -> Dict:
        """
        Analyze failure modes with probability and impact.
        
        Args:
            failure_modes: Dict of {mode: (probability, impact)}
            
        Returns:
            Risk assessment dictionary
        """
        risks = {}
        total_risk = 0
        
        for mode, (prob, impact) in failure_modes.items():
            risk_score = prob * impact
            risks[mode] = {
                'probability': prob,
                'impact': impact,
                'risk_score': risk_score,
                'expected_loss': risk_score
            }
            total_risk += risk_score
        
        # Sort by risk score
        sorted_risks = sorted(risks.items(), key=lambda x: x[1]['risk_score'], reverse=True)
        
        return {
            'failure_modes': dict(sorted_risks),
            'total_expected_loss': total_risk,
            'highest_risk': sorted_risks[0][0] if sorted_risks else None,
            'highest_probability': max(failure_modes.items(), key=lambda x: x[1][0])[0],
            'highest_impact': max(failure_modes.items(), key=lambda x: x[1][1])[0]
        }
    
    def bayesian_update(self,
                       prior: float,
                       likelihood_given_true: float,
                       likelihood_given_false: float) -> float:
        """
        Update probability given new evidence.
        
        Args:
            prior: Prior probability
            likelihood_given_true: P(evidence|hypothesis true)
            likelihood_given_false: P(evidence|hypothesis false)
            
        Returns:
            Posterior probability
        """
        evidence = (likelihood_given_true * prior + 
                   likelihood_given_false * (1 - prior))
        
        if evidence == 0:
            return prior
            
        posterior = (likelihood_given_true * prior) / evidence
        return posterior
    
    def calculate_sample_size(self,
                            effect_size: float,
                            power: float = 0.8,
                            alpha: float = 0.05) -> int:
        """
        Calculate required sample size for statistical power.
        
        Args:
            effect_size: Minimum detectable effect (Cohen's d)
            power: Statistical power (1 - Type II error rate)
            alpha: Significance level (Type I error rate)
            
        Returns:
            Required sample size per group
        """
        from scipy import stats
        
        z_alpha = stats.norm.ppf(1 - alpha/2)
        z_beta = stats.norm.ppf(power)
        
        n = ((z_alpha + z_beta) ** 2 * 2) / (effect_size ** 2)
        return int(np.ceil(n))
    
    def adjust_for_base_rate(self,
                            optimistic_projection: float,
                            scenario_type: str) -> float:
        """
        Adjust projections using historical base rates.
        
        Args:
            optimistic_projection: Original projection
            scenario_type: Type of scenario for base rate
            
        Returns:
            Reality-adjusted projection
        """
        if scenario_type in self.base_rates:
            base_rate = self.base_rates[scenario_type]
            # Weight: 70% base rate, 30% projection
            adjusted = base_rate * 0.7 + optimistic_projection * 0.3
        else:
            # Unknown scenario: divide by 3 (conservative)
            adjusted = optimistic_projection / 3
        
        return adjusted
    
    def calculate_confidence_interval(self,
                                    estimate: float,
                                    standard_error: float,
                                    sample_size: int) -> Tuple[float, float]:
        """
        Calculate confidence interval for estimate.
        
        Args:
            estimate: Point estimate
            standard_error: Standard error
            sample_size: Sample size
            
        Returns:
            (lower_bound, upper_bound)
        """
        from scipy import stats
        
        # Use t-distribution for small samples
        if sample_size < 30:
            critical_value = stats.t.ppf(1 - (1 - self.confidence_level) / 2, sample_size - 1)
        else:
            critical_value = stats.norm.ppf(1 - (1 - self.confidence_level) / 2)
        
        margin = critical_value * standard_error
        return (estimate - margin, estimate + margin)


def main():
    """Example usage of risk analyzer."""
    analyzer = RiskAnalyzer()
    
    # Example: Analyze a new product launch
    print("=== New Product Launch Risk Analysis ===\n")
    
    # Failure modes
    failure_modes = {
        'market_rejection': (0.6, 0.9),
        'technical_issues': (0.3, 0.7),
        'competition': (0.4, 0.6),
        'regulatory': (0.2, 1.0),
        'supply_chain': (0.25, 0.5)
    }
    
    failure_analysis = analyzer.failure_mode_analysis(failure_modes)
    print(f"Highest risk: {failure_analysis['highest_risk']}")
    print(f"Total expected loss: {failure_analysis['total_expected_loss']:.2%}\n")
    
    # Revenue projection with Monte Carlo
    print("=== Revenue Projection Analysis ===\n")
    revenue_projection = 10_000_000  # $10M optimistic projection
    
    # Adjust for base rate
    adjusted = analyzer.adjust_for_base_rate(revenue_projection, 'new_product_success')
    print(f"Optimistic projection: ${revenue_projection:,.0f}")
    print(f"Base-rate adjusted: ${adjusted:,.0f}\n")
    
    # Run simulation
    simulation = analyzer.monte_carlo_simulation(adjusted, volatility=0.5)
    print(f"Monte Carlo Results (10,000 simulations):")
    print(f"  Median outcome: ${simulation['p50']:,.0f}")
    print(f"  90% confidence range: ${simulation['p5']:,.0f} - ${simulation['p95']:,.0f}")
    print(f"  Probability of loss: {simulation['probability_loss']:.1%}")
    print(f"  Worst case (1%): ${simulation['conditional_var_95']:,.0f}\n")
    
    # Success probability calculation
    print("=== Success Probability ===\n")
    required_successes = {
        'product_market_fit': 0.4,
        'technical_execution': 0.7,
        'marketing_effectiveness': 0.3,
        'funding_secured': 0.6
    }
    
    joint_prob = analyzer.calculate_joint_probability(list(required_successes.values()))
    print(f"Required successes: {list(required_successes.keys())}")
    print(f"Individual probabilities: {list(required_successes.values())}")
    print(f"Joint probability of success: {joint_prob:.2%}\n")
    
    # Sample size for validation
    print("=== Validation Requirements ===")
    sample_size = analyzer.calculate_sample_size(effect_size=0.5)
    print(f"Sample size needed for 80% power: {sample_size} per group")


if __name__ == "__main__":
    main()