#!/usr/bin/env python3
"""
Domain Expert Adaptive Analyzer
Context-aware domain-specific calculations and analysis
"""

import math
import numpy as np
from typing import Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass
import json

class DomainType(Enum):
    """Types of domain expertise."""
    TECHNICAL = "technical"
    FINANCIAL = "financial"
    LEGAL = "legal"
    PRODUCT = "product"
    DATA = "data"
    INDUSTRY = "industry"
    PEOPLE = "people"
    CONTRARIAN = "contrarian"

class DomainAnalyzer:
    """Adaptive analyzer that switches based on domain context."""
    
    def __init__(self):
        self.domain_keywords = {
            DomainType.TECHNICAL: ['api', 'architecture', 'scalability', 'technical debt', 
                                  'infrastructure', 'latency', 'microservices', 'deployment'],
            DomainType.FINANCIAL: ['revenue', 'valuation', 'burn rate', 'runway', 'CAC',
                                  'LTV', 'margins', 'fundraising', 'unit economics'],
            DomainType.LEGAL: ['compliance', 'regulatory', 'liability', 'contract', 'IP',
                             'patent', 'litigation', 'terms', 'privacy'],
            DomainType.PRODUCT: ['feature', 'user experience', 'roadmap', 'design', 'MVP',
                               'product-market fit', 'retention', 'activation'],
            DomainType.DATA: ['analytics', 'metrics', 'ML', 'AI', 'data pipeline',
                            'insights', 'dashboard', 'prediction', 'model']
        }
        
    def detect_domain(self, context: str) -> DomainType:
        """
        Detect which domain expertise is needed based on context.
        
        Args:
            context: Description of the decision/problem
            
        Returns:
            Most relevant domain type
        """
        context_lower = context.lower()
        scores = {}
        
        for domain, keywords in self.domain_keywords.items():
            score = sum(1 for keyword in keywords if keyword in context_lower)
            scores[domain] = score
        
        if max(scores.values()) == 0:
            return DomainType.INDUSTRY  # Default to industry veteran
            
        return max(scores, key=scores.get)
    
    def analyze(self, domain: DomainType, parameters: Dict) -> Dict:
        """
        Perform domain-specific analysis.
        
        Args:
            domain: Type of expertise needed
            parameters: Domain-specific parameters
            
        Returns:
            Analysis results
        """
        analyzers = {
            DomainType.TECHNICAL: self._technical_analysis,
            DomainType.FINANCIAL: self._financial_analysis,
            DomainType.LEGAL: self._legal_analysis,
            DomainType.PRODUCT: self._product_analysis,
            DomainType.DATA: self._data_analysis,
            DomainType.INDUSTRY: self._industry_analysis
        }
        
        analyzer = analyzers.get(domain, self._industry_analysis)
        return analyzer(parameters)
    
    def _technical_analysis(self, params: Dict) -> Dict:
        """Perform technical architecture analysis."""
        
        # Scale analysis
        current_users = params.get('current_users', 1000)
        target_users = params.get('target_users', 1000000)
        scale_factor = target_users / current_users
        
        # Architecture recommendations
        if target_users < 100000:
            architecture = "Monolith"
            complexity = "Low"
            team_size = "3-5 engineers"
        elif target_users < 1000000:
            architecture = "Service-Oriented"
            complexity = "Medium"
            team_size = "10-20 engineers"
        elif target_users < 10000000:
            architecture = "Microservices"
            complexity = "High"
            team_size = "30-50 engineers"
        else:
            architecture = "Platform"
            complexity = "Very High"
            team_size = "100+ engineers"
        
        # Performance calculations
        current_latency = params.get('current_latency_ms', 100)
        projected_latency = current_latency * math.log10(scale_factor + 1)
        
        # Technical debt assessment
        codebase_age_months = params.get('codebase_age_months', 12)
        tech_debt_ratio = min(0.5, codebase_age_months / 100)
        refactor_cost_months = tech_debt_ratio * 6
        
        # Scaling costs
        infrastructure_cost = current_users * 0.01  # $0.01 per user baseline
        scaled_cost = infrastructure_cost * (scale_factor ** 0.7)  # Economies of scale
        
        return {
            'recommended_architecture': architecture,
            'complexity_level': complexity,
            'required_team_size': team_size,
            'scale_factor': scale_factor,
            'projected_latency_ms': round(projected_latency),
            'performance_degradation': f"{(projected_latency/current_latency - 1)*100:.1f}%",
            'technical_debt_ratio': f"{tech_debt_ratio*100:.1f}%",
            'refactoring_investment_months': round(refactor_cost_months, 1),
            'monthly_infrastructure_cost': f"${scaled_cost:,.0f}",
            'cost_per_user': f"${scaled_cost/target_users:.3f}",
            'bottlenecks': self._identify_bottlenecks(scale_factor),
            'technology_recommendations': self._tech_stack_recommendations(target_users)
        }
    
    def _identify_bottlenecks(self, scale_factor: float) -> List[str]:
        """Identify likely bottlenecks at scale."""
        bottlenecks = []
        
        if scale_factor > 10:
            bottlenecks.append("Database connections")
        if scale_factor > 50:
            bottlenecks.append("API rate limits")
        if scale_factor > 100:
            bottlenecks.append("Cache invalidation")
        if scale_factor > 500:
            bottlenecks.append("Network bandwidth")
        if scale_factor > 1000:
            bottlenecks.append("Geographic distribution")
            
        return bottlenecks
    
    def _tech_stack_recommendations(self, users: int) -> Dict:
        """Recommend technology stack based on scale."""
        if users < 10000:
            return {
                'hosting': 'Heroku/Vercel',
                'database': 'PostgreSQL',
                'cache': 'Redis',
                'monitoring': 'Datadog'
            }
        elif users < 100000:
            return {
                'hosting': 'AWS/GCP',
                'database': 'PostgreSQL + Read Replicas',
                'cache': 'Redis Cluster',
                'monitoring': 'Datadog + Custom'
            }
        elif users < 1000000:
            return {
                'hosting': 'Kubernetes on AWS/GCP',
                'database': 'PostgreSQL + Sharding',
                'cache': 'Redis + CDN',
                'monitoring': 'Prometheus + Grafana'
            }
        else:
            return {
                'hosting': 'Multi-region Kubernetes',
                'database': 'Distributed (Cassandra/Spanner)',
                'cache': 'Multi-layer (Redis + CDN + Edge)',
                'monitoring': 'Custom observability platform'
            }
    
    def _financial_analysis(self, params: Dict) -> Dict:
        """Perform financial modeling and analysis."""
        
        # Revenue metrics
        mrr = params.get('mrr', 10000)
        growth_rate = params.get('growth_rate_monthly', 0.15)
        churn_rate = params.get('churn_rate_monthly', 0.05)
        
        # Calculate key SaaS metrics
        arr = mrr * 12
        net_revenue_retention = 1 - churn_rate + (growth_rate * 0.3)  # Expansion estimate
        
        # LTV/CAC calculation
        arpu = params.get('arpu', 100)
        gross_margin = params.get('gross_margin', 0.8)
        cac = params.get('cac', 500)
        
        customer_lifetime_months = 1 / churn_rate if churn_rate > 0 else 120
        ltv = arpu * gross_margin * customer_lifetime_months
        ltv_cac_ratio = ltv / cac if cac > 0 else 0
        
        # Burn rate and runway
        monthly_burn = params.get('monthly_burn', 50000)
        cash_balance = params.get('cash_balance', 1000000)
        
        months_to_profitability = self._calculate_profitability_timeline(
            mrr, growth_rate, monthly_burn, gross_margin
        )
        
        runway_months = cash_balance / (monthly_burn - mrr * gross_margin)
        
        # Valuation estimate (using revenue multiples)
        if growth_rate > 0.5:
            multiple = 20
        elif growth_rate > 0.3:
            multiple = 15
        elif growth_rate > 0.2:
            multiple = 10
        elif growth_rate > 0.1:
            multiple = 6
        else:
            multiple = 3
            
        estimated_valuation = arr * multiple
        
        # Fundraising recommendations
        if runway_months < 6:
            fundraising_urgency = "Critical"
            recommended_raise = monthly_burn * 24
        elif runway_months < 12:
            fundraising_urgency = "High"
            recommended_raise = monthly_burn * 18
        elif runway_months < 18:
            fundraising_urgency = "Medium"
            recommended_raise = monthly_burn * 18
        else:
            fundraising_urgency = "Low"
            recommended_raise = monthly_burn * 12
        
        return {
            'current_arr': f"${arr:,.0f}",
            'growth_rate': f"{growth_rate*100:.1f}%",
            'net_revenue_retention': f"{net_revenue_retention*100:.1f}%",
            'ltv': f"${ltv:,.0f}",
            'cac': f"${cac:,.0f}",
            'ltv_cac_ratio': f"{ltv_cac_ratio:.1f}",
            'ltv_cac_health': 'Healthy' if ltv_cac_ratio > 3 else 'Concerning',
            'cac_payback_months': round(cac / (arpu * gross_margin), 1),
            'burn_multiple': round(monthly_burn / (mrr * growth_rate), 1) if mrr * growth_rate > 0 else 'N/A',
            'runway_months': round(runway_months, 1),
            'months_to_profitability': months_to_profitability,
            'estimated_valuation': f"${estimated_valuation:,.0f}",
            'valuation_multiple': f"{multiple}x ARR",
            'fundraising_urgency': fundraising_urgency,
            'recommended_raise': f"${recommended_raise:,.0f}",
            'rule_of_40': f"{(growth_rate*100 + (1-monthly_burn/mrr)*100):.1f}" if mrr > 0 else 'N/A'
        }
    
    def _calculate_profitability_timeline(self, mrr: float, growth: float, 
                                         burn: float, margin: float) -> str:
        """Calculate when company reaches profitability."""
        months = 0
        current_mrr = mrr
        
        while months < 60:  # Cap at 5 years
            net = current_mrr * margin - burn
            if net >= 0:
                return f"{months} months"
            current_mrr *= (1 + growth)
            months += 1
            
        return "Not within 5 years"
    
    def _legal_analysis(self, params: Dict) -> Dict:
        """Perform legal and regulatory analysis."""
        
        industry = params.get('industry', 'general')
        jurisdictions = params.get('jurisdictions', ['US'])
        data_types = params.get('data_types', [])
        
        # Compliance requirements
        requirements = []
        compliance_cost = 0
        timeline_months = 3
        
        # Industry-specific regulations
        industry_reqs = {
            'healthcare': ['HIPAA', 'FDA', 'State licensing'],
            'finance': ['SEC', 'FINRA', 'KYC/AML'],
            'education': ['FERPA', 'COPPA', 'State certification']
        }
        
        if industry in industry_reqs:
            requirements.extend(industry_reqs[industry])
            compliance_cost += 100000
            timeline_months += 6
        
        # Data privacy regulations
        if 'personal' in data_types:
            if 'EU' in jurisdictions:
                requirements.append('GDPR')
                compliance_cost += 50000
            if 'CA' in jurisdictions or 'US' in jurisdictions:
                requirements.append('CCPA')
                compliance_cost += 30000
        
        # IP strategy
        ip_strategy = self._determine_ip_strategy(params)
        
        # Risk assessment
        risk_score = 0
        risk_factors = []
        
        if len(requirements) > 3:
            risk_score += 30
            risk_factors.append("Complex regulatory environment")
        
        if 'financial' in data_types:
            risk_score += 20
            risk_factors.append("Financial data liability")
            
        if 'health' in data_types:
            risk_score += 25
            risk_factors.append("Health data liability")
        
        return {
            'compliance_requirements': requirements,
            'estimated_compliance_cost': f"${compliance_cost:,}",
            'compliance_timeline': f"{timeline_months} months",
            'ip_strategy': ip_strategy,
            'regulatory_risk_score': risk_score,
            'risk_level': self._get_risk_level(risk_score),
            'risk_factors': risk_factors,
            'recommended_structure': self._recommend_structure(params),
            'insurance_recommendations': self._insurance_recommendations(industry, risk_score)
        }
    
    def _determine_ip_strategy(self, params: Dict) -> Dict:
        """Determine intellectual property strategy."""
        has_novel_tech = params.get('novel_technology', False)
        competitive_advantage = params.get('competitive_advantage_years', 2)
        
        if has_novel_tech and competitive_advantage > 5:
            return {
                'approach': 'Patent portfolio',
                'reasoning': 'Long-term competitive advantage from novel technology'
            }
        elif has_novel_tech and competitive_advantage <= 5:
            return {
                'approach': 'Trade secrets',
                'reasoning': 'Short advantage window, keep proprietary'
            }
        else:
            return {
                'approach': 'Execution focus',
                'reasoning': 'No novel IP, compete on execution'
            }
    
    def _recommend_structure(self, params: Dict) -> str:
        """Recommend corporate structure."""
        revenue = params.get('revenue', 0)
        investors = params.get('has_investors', False)
        
        if investors or revenue > 1000000:
            return "Delaware C-Corp"
        elif revenue > 100000:
            return "Delaware LLC"
        else:
            return "Local LLC"
    
    def _insurance_recommendations(self, industry: str, risk_score: int) -> List[str]:
        """Recommend insurance coverage."""
        base = ['General Liability', 'Cyber Liability']
        
        if risk_score > 50:
            base.append('Errors & Omissions')
        if industry in ['healthcare', 'finance']:
            base.append('Professional Liability')
        if risk_score > 70:
            base.append('Directors & Officers')
            
        return base
    
    def _product_analysis(self, params: Dict) -> Dict:
        """Perform product and user experience analysis."""
        
        # Product metrics
        dau = params.get('daily_active_users', 1000)
        mau = params.get('monthly_active_users', 5000)
        
        # Engagement metrics
        dau_mau_ratio = dau / mau if mau > 0 else 0
        
        # Retention cohorts
        d1_retention = params.get('d1_retention', 0.6)
        d7_retention = params.get('d7_retention', 0.3)
        d30_retention = params.get('d30_retention', 0.15)
        
        # Product-market fit indicators
        pmf_score = 0
        pmf_indicators = []
        
        if d30_retention > 0.2:
            pmf_score += 30
            pmf_indicators.append("Strong retention")
            
        if params.get('nps', 0) > 30:
            pmf_score += 25
            pmf_indicators.append("High NPS")
            
        if params.get('organic_growth_percent', 0) > 0.3:
            pmf_score += 25
            pmf_indicators.append("Strong organic growth")
            
        if dau_mau_ratio > 0.4:
            pmf_score += 20
            pmf_indicators.append("High engagement")
        
        # Feature prioritization
        features = params.get('proposed_features', [])
        prioritized = self._prioritize_features(features)
        
        return {
            'dau_mau_ratio': f"{dau_mau_ratio*100:.1f}%",
            'engagement_level': self._get_engagement_level(dau_mau_ratio),
            'd1_retention': f"{d1_retention*100:.1f}%",
            'd7_retention': f"{d7_retention*100:.1f}%",
            'd30_retention': f"{d30_retention*100:.1f}%",
            'retention_health': self._assess_retention_health(d1_retention, d7_retention, d30_retention),
            'pmf_score': pmf_score,
            'pmf_status': 'Strong' if pmf_score > 70 else 'Emerging' if pmf_score > 40 else 'Not yet',
            'pmf_indicators': pmf_indicators,
            'prioritized_features': prioritized,
            'recommended_focus': self._recommend_product_focus(pmf_score, d30_retention)
        }
    
    def _get_engagement_level(self, ratio: float) -> str:
        """Categorize engagement level."""
        if ratio > 0.5:
            return "Very High"
        elif ratio > 0.3:
            return "High"
        elif ratio > 0.15:
            return "Medium"
        else:
            return "Low"
    
    def _assess_retention_health(self, d1: float, d7: float, d30: float) -> str:
        """Assess retention curve health."""
        if d30 > 0.2 and d7 > 0.35 and d1 > 0.7:
            return "Excellent"
        elif d30 > 0.1 and d7 > 0.2 and d1 > 0.5:
            return "Good"
        else:
            return "Needs improvement"
    
    def _prioritize_features(self, features: List[Dict]) -> List[str]:
        """Prioritize features using RICE framework."""
        if not features:
            return []
            
        for feature in features:
            reach = feature.get('reach', 1000)
            impact = feature.get('impact', 2)  # 0.25, 0.5, 1, 2, 3
            confidence = feature.get('confidence', 0.8)
            effort = feature.get('effort', 5)
            
            feature['rice_score'] = (reach * impact * confidence) / effort
        
        sorted_features = sorted(features, key=lambda x: x['rice_score'], reverse=True)
        return [f"{f.get('name', 'Unknown')}: {f['rice_score']:.0f}" for f in sorted_features[:5]]
    
    def _recommend_product_focus(self, pmf_score: int, retention: float) -> str:
        """Recommend product development focus."""
        if pmf_score < 40:
            return "Focus on core value proposition and retention"
        elif pmf_score < 70:
            return "Improve activation and early retention"
        else:
            return "Scale and optimize for growth"
    
    def _data_analysis(self, params: Dict) -> Dict:
        """Perform data and analytics analysis."""
        
        data_volume_gb = params.get('data_volume_gb', 100)
        data_growth_rate = params.get('data_growth_monthly', 0.2)
        
        # Determine analytics maturity
        has_dashboards = params.get('has_dashboards', False)
        has_ml = params.get('has_ml', False)
        has_predictions = params.get('has_predictions', False)
        
        maturity_level = 1
        if has_dashboards:
            maturity_level = 2
        if has_ml:
            maturity_level = 3
        if has_predictions:
            maturity_level = 4
        
        # Infrastructure recommendations
        if data_volume_gb < 100:
            infra_rec = "Cloud data warehouse (BigQuery/Snowflake)"
        elif data_volume_gb < 1000:
            infra_rec = "Dedicated cluster (Spark/Databricks)"
        else:
            infra_rec = "Data lake architecture (S3 + Spark + Presto)"
        
        # ML readiness
        ml_ready = data_volume_gb > 10 and maturity_level >= 2
        
        return {
            'current_data_volume': f"{data_volume_gb} GB",
            'projected_volume_1y': f"{data_volume_gb * (1 + data_growth_rate)**12:.0f} GB",
            'analytics_maturity': f"Level {maturity_level}/5",
            'maturity_description': self._get_maturity_description(maturity_level),
            'infrastructure_recommendation': infra_rec,
            'ml_readiness': 'Ready' if ml_ready else 'Not ready',
            'next_steps': self._data_next_steps(maturity_level),
            'estimated_monthly_cost': f"${data_volume_gb * 20 + maturity_level * 1000}"
        }
    
    def _get_maturity_description(self, level: int) -> str:
        """Describe analytics maturity level."""
        descriptions = {
            1: "Basic reporting",
            2: "Diagnostic analytics",
            3: "Predictive analytics",
            4: "Prescriptive analytics",
            5: "Cognitive analytics"
        }
        return descriptions.get(level, "Unknown")
    
    def _data_next_steps(self, level: int) -> List[str]:
        """Recommend next steps for data maturity."""
        steps = {
            1: ["Implement tracking", "Build dashboards", "Define KPIs"],
            2: ["Add cohort analysis", "Build data pipeline", "Implement A/B testing"],
            3: ["Develop ML models", "Automate insights", "Real-time analytics"],
            4: ["Optimization algorithms", "Automated decisions", "AI integration"],
            5: ["Self-learning systems", "Autonomous optimization"]
        }
        return steps.get(level, [])
    
    def _industry_analysis(self, params: Dict) -> Dict:
        """Perform industry and market analysis."""
        
        market_size = params.get('total_addressable_market', 1000000000)
        market_growth = params.get('market_growth_rate', 0.1)
        competitors = params.get('competitor_count', 10)
        market_share = params.get('current_market_share', 0.01)
        
        # Market dynamics
        if competitors < 3:
            market_structure = "Oligopoly"
            competitive_intensity = "Low"
        elif competitors < 10:
            market_structure = "Concentrated"
            competitive_intensity = "Medium"
        else:
            market_structure = "Fragmented"
            competitive_intensity = "High"
        
        # Growth strategy recommendation
        if market_share < 0.01:
            strategy = "Land grab - focus on growth over profit"
        elif market_share < 0.1:
            strategy = "Expand and defend - balance growth and efficiency"
        else:
            strategy = "Optimize and differentiate - focus on profitability"
        
        return {
            'market_size': f"${market_size:,.0f}",
            'market_growth': f"{market_growth*100:.1f}%",
            'market_structure': market_structure,
            'competitive_intensity': competitive_intensity,
            'current_position': f"{market_share*100:.2f}% market share",
            'recommended_strategy': strategy,
            'market_opportunity': f"${market_size * market_share * 10:,.0f}",
            'time_to_saturation': f"{math.log(0.5/market_share) / math.log(1 + market_growth):.1f} years" if market_growth > 0 else "N/A"
        }
    
    def _get_risk_level(self, score: float) -> str:
        """Convert risk score to level."""
        if score >= 70:
            return "Critical"
        elif score >= 50:
            return "High"
        elif score >= 30:
            return "Medium"
        else:
            return "Low"


def main():
    """Example usage of domain analyzer."""
    analyzer = DomainAnalyzer()
    
    # Detect domain from context
    context = "We need to improve our API architecture to handle 10x growth while reducing technical debt"
    domain = analyzer.detect_domain(context)
    
    print(f"=== Domain Expert Analysis ===")
    print(f"Context: {context}")
    print(f"Detected Domain: {domain.value.title()}\n")
    
    # Technical analysis example
    if domain == DomainType.TECHNICAL:
        params = {
            'current_users': 10000,
            'target_users': 1000000,
            'current_latency_ms': 50,
            'codebase_age_months': 24
        }
        
        results = analyzer.analyze(domain, params)
        
        print("Technical Assessment:")
        print(f"  Architecture: {results['recommended_architecture']}")
        print(f"  Team Size Needed: {results['required_team_size']}")
        print(f"  Scale Factor: {results['scale_factor']}x")
        print(f"  Infrastructure Cost: {results['monthly_infrastructure_cost']}/month")
        print(f"  Technical Debt: {results['technical_debt_ratio']}")
        print(f"  Refactoring Investment: {results['refactoring_investment_months']} months")
        print(f"  Bottlenecks: {', '.join(results['bottlenecks'])}")
        
    # Financial analysis example
    print("\n=== Financial Analysis ===")
    financial_params = {
        'mrr': 50000,
        'growth_rate_monthly': 0.20,
        'churn_rate_monthly': 0.03,
        'arpu': 100,
        'gross_margin': 0.75,
        'cac': 800,
        'monthly_burn': 100000,
        'cash_balance': 2000000
    }
    
    financial_results = analyzer.analyze(DomainType.FINANCIAL, financial_params)
    
    print("Financial Metrics:")
    print(f"  ARR: {financial_results['current_arr']}")
    print(f"  LTV/CAC: {financial_results['ltv_cac_ratio']}")
    print(f"  Runway: {financial_results['runway_months']} months")
    print(f"  Valuation: {financial_results['estimated_valuation']}")
    print(f"  Fundraising: {financial_results['fundraising_urgency']}")
    print(f"  Recommended Raise: {financial_results['recommended_raise']}")


if __name__ == "__main__":
    main()