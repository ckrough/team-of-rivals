#!/usr/bin/env python3
"""
COMPASS Ethical Assessment Calculator
Stakeholder impact and ethical scoring tools
"""

import numpy as np
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum
import json

class StakeholderGroup(Enum):
    """Stakeholder categories with default weights."""
    CUSTOMERS = ("Customers", 0.30)
    EMPLOYEES = ("Employees", 0.25)
    SHAREHOLDERS = ("Shareholders", 0.20)
    COMMUNITY = ("Community", 0.15)
    ENVIRONMENT = ("Environment", 0.10)
    SUPPLIERS = ("Suppliers", 0.05)
    COMPETITORS = ("Competitors", 0.05)
    FUTURE_GEN = ("Future Generations", 0.10)
    REGULATORS = ("Regulators", 0.05)
    
    def __init__(self, label, default_weight):
        self.label = label
        self.default_weight = default_weight

@dataclass
class StakeholderImpact:
    """Impact on a specific stakeholder group."""
    group: StakeholderGroup
    immediate_impact: float  # -5 to +5
    long_term_impact: float  # -5 to +5
    reversible: bool
    has_consent: bool
    power_differential: str  # 'high', 'medium', 'low'
    affected_count: int
    
    @property
    def net_impact(self) -> float:
        """Calculate weighted net impact."""
        # Weight long-term more heavily
        return (self.immediate_impact * 0.3 + self.long_term_impact * 0.7)
    
    @property
    def risk_score(self) -> float:
        """Calculate risk based on negative impact and irreversibility."""
        if self.net_impact >= 0:
            return 0
        
        risk = abs(self.net_impact)
        
        if not self.reversible:
            risk *= 2
        
        if not self.has_consent:
            risk *= 1.5
            
        if self.power_differential == 'high':
            risk *= 1.3
            
        return risk

class EthicalAssessment:
    """Comprehensive ethical evaluation system."""
    
    def __init__(self):
        self.trust_weights = {
            'credibility': 0.25,
            'reliability': 0.25,
            'intimacy': 0.25,
            'self_orientation': 0.25
        }
        
    def calculate_stakeholder_score(self, 
                                   impacts: List[StakeholderImpact],
                                   custom_weights: Optional[Dict] = None) -> Dict:
        """
        Calculate aggregate stakeholder impact score.
        
        Args:
            impacts: List of stakeholder impacts
            custom_weights: Optional custom weights by group
            
        Returns:
            Comprehensive stakeholder analysis
        """
        # Use custom weights or defaults
        weights = custom_weights or {
            sg: sg.default_weight for sg in StakeholderGroup
        }
        
        total_benefit = 0
        total_harm = 0
        weighted_score = 0
        
        impact_by_group = {}
        
        for impact in impacts:
            weight = weights.get(impact.group, impact.group.default_weight)
            
            # Separate benefits and harms
            if impact.net_impact > 0:
                total_benefit += impact.net_impact * weight
            else:
                total_harm += abs(impact.net_impact) * weight
            
            weighted_score += impact.net_impact * weight
            
            impact_by_group[impact.group.label] = {
                'immediate': impact.immediate_impact,
                'long_term': impact.long_term_impact,
                'net_impact': impact.net_impact,
                'risk_score': impact.risk_score,
                'reversible': impact.reversible,
                'has_consent': impact.has_consent,
                'affected_count': impact.affected_count
            }
        
        # Calculate distribution metrics
        gini = self._calculate_gini_coefficient(impacts)
        
        return {
            'weighted_score': weighted_score,
            'total_benefit': total_benefit,
            'total_harm': total_harm,
            'benefit_harm_ratio': total_benefit / total_harm if total_harm > 0 else float('inf'),
            'gini_coefficient': gini,
            'impacts_by_group': impact_by_group,
            'most_benefited': max(impacts, key=lambda x: x.net_impact).group.label,
            'most_harmed': min(impacts, key=lambda x: x.net_impact).group.label,
            'total_affected': sum(i.affected_count for i in impacts)
        }
    
    def _calculate_gini_coefficient(self, impacts: List[StakeholderImpact]) -> float:
        """Calculate inequality in impact distribution."""
        values = sorted([i.net_impact + 5 for i in impacts])  # Shift to positive
        n = len(values)
        index = np.arange(1, n + 1)
        return (2 * np.sum(index * values)) / (n * np.sum(values)) - (n + 1) / n
    
    def apply_ethical_frameworks(self, 
                                decision: str,
                                context: Dict) -> Dict:
        """
        Apply multiple ethical frameworks to a decision.
        
        Args:
            decision: Description of the decision
            context: Contextual information
            
        Returns:
            Multi-framework ethical analysis
        """
        results = {}
        
        # Utilitarian analysis
        results['utilitarian'] = self._utilitarian_analysis(context)
        
        # Deontological analysis
        results['deontological'] = self._deontological_analysis(context)
        
        # Virtue ethics analysis
        results['virtue_ethics'] = self._virtue_analysis(context)
        
        # Rawlsian analysis
        results['rawlsian'] = self._rawlsian_analysis(context)
        
        # Aggregate recommendation
        scores = [r['score'] for r in results.values()]
        results['aggregate_score'] = np.mean(scores)
        results['recommendation'] = self._get_recommendation(results['aggregate_score'])
        
        return results
    
    def _utilitarian_analysis(self, context: Dict) -> Dict:
        """Apply utilitarian framework."""
        # Calculate total utility
        pleasure = context.get('total_benefit', 0)
        pain = context.get('total_harm', 0)
        extent = context.get('affected_count', 1)
        duration = context.get('impact_duration_years', 1)
        certainty = context.get('probability', 1)
        
        utility = (pleasure - pain) * extent * duration * certainty
        
        return {
            'score': max(0, min(100, 50 + utility / 100)),
            'utility': utility,
            'assessment': 'Net positive' if utility > 0 else 'Net negative'
        }
    
    def _deontological_analysis(self, context: Dict) -> Dict:
        """Apply deontological framework."""
        score = 100
        violations = []
        
        # Check for rights violations
        if not context.get('respects_autonomy', True):
            score -= 30
            violations.append('Violates autonomy')
            
        if not context.get('truthful', True):
            score -= 25
            violations.append('Involves deception')
            
        if context.get('uses_people_as_means', False):
            score -= 40
            violations.append('Treats people as means only')
            
        # Universal law test
        if not context.get('universalizable', True):
            score -= 30
            violations.append('Fails universalizability test')
        
        return {
            'score': max(0, score),
            'violations': violations,
            'assessment': 'Permissible' if score > 50 else 'Impermissible'
        }
    
    def _virtue_analysis(self, context: Dict) -> Dict:
        """Apply virtue ethics framework."""
        virtues = {
            'courage': context.get('demonstrates_courage', 5) / 10,
            'temperance': context.get('demonstrates_temperance', 5) / 10,
            'justice': context.get('demonstrates_justice', 5) / 10,
            'prudence': context.get('demonstrates_prudence', 5) / 10,
            'integrity': context.get('demonstrates_integrity', 5) / 10
        }
        
        virtue_score = np.mean(list(virtues.values())) * 100
        
        return {
            'score': virtue_score,
            'virtues': virtues,
            'assessment': 'Virtuous' if virtue_score > 60 else 'Lacks virtue'
        }
    
    def _rawlsian_analysis(self, context: Dict) -> Dict:
        """Apply Rawlsian framework."""
        score = 100
        
        # Check if benefits least advantaged
        if not context.get('benefits_least_advantaged', False):
            score -= 40
            
        # Check equality of opportunity
        if not context.get('equal_opportunity', True):
            score -= 30
            
        # Check basic liberties
        if not context.get('preserves_liberties', True):
            score -= 30
            
        # Veil of ignorance test
        if not context.get('passes_veil_test', True):
            score -= 25
        
        return {
            'score': max(0, score),
            'difference_principle': context.get('benefits_least_advantaged', False),
            'assessment': 'Just' if score > 50 else 'Unjust'
        }
    
    def _get_recommendation(self, score: float) -> str:
        """Convert score to recommendation."""
        if score >= 80:
            return "Strongly Recommended"
        elif score >= 60:
            return "Recommended with Modifications"
        elif score >= 40:
            return "Proceed with Caution"
        elif score >= 20:
            return "Not Recommended"
        else:
            return "Strongly Opposed"
    
    def calculate_trust_score(self,
                             credibility: float,
                             reliability: float,
                             intimacy: float,
                             self_orientation: float) -> float:
        """
        Calculate trust score using Maister formula.
        
        Args:
            credibility: 0-10 scale
            reliability: 0-10 scale
            intimacy: 0-10 scale
            self_orientation: 0-10 scale (lower is better)
            
        Returns:
            Trust score (0-100)
        """
        if self_orientation == 0:
            self_orientation = 0.1  # Avoid division by zero
            
        trust = ((credibility + reliability + intimacy) / 3) / (self_orientation / 5)
        return min(100, trust * 10)
    
    def project_reputation_impact(self,
                                 current_reputation: float,
                                 decision_impact: float,
                                 years: int = 10) -> Dict:
        """
        Project reputation trajectory over time.
        
        Args:
            current_reputation: Current score (0-100)
            decision_impact: Impact of decision (-50 to +50)
            years: Projection period
            
        Returns:
            Reputation trajectory
        """
        trajectory = []
        reputation = current_reputation
        
        for year in range(years + 1):
            if year == 0:
                # Immediate impact
                reputation += decision_impact
            else:
                # Recovery/decay over time
                if decision_impact < 0:
                    # Negative impacts recover slowly
                    reputation += min(2, (100 - reputation) * 0.1)
                else:
                    # Positive impacts decay slowly  
                    reputation -= max(0, (reputation - current_reputation) * 0.05)
            
            reputation = max(0, min(100, reputation))
            trajectory.append({
                'year': year,
                'reputation': round(reputation, 1)
            })
        
        return {
            'trajectory': trajectory,
            'final_reputation': trajectory[-1]['reputation'],
            'recovery_years': next((t['year'] for t in trajectory 
                                  if t['reputation'] >= current_reputation), None),
            'permanent_damage': decision_impact < -30
        }
    
    def analyze_regulatory_risk(self,
                               current_compliance: bool,
                               public_sentiment: float,
                               incident_rate: float,
                               lobby_strength: float) -> Dict:
        """
        Analyze regulatory risk and trajectory.
        
        Args:
            current_compliance: Currently compliant
            public_sentiment: Negative sentiment (0-1)
            incident_rate: Incidents per year
            lobby_strength: Industry lobby power (0-1)
            
        Returns:
            Regulatory risk analysis
        """
        # Base risk from current factors
        risk_score = 0
        
        if not current_compliance:
            risk_score += 40
        
        risk_score += public_sentiment * 30
        risk_score += min(30, incident_rate * 10)
        risk_score -= lobby_strength * 20
        
        risk_score = max(0, min(100, risk_score))
        
        # Timeline predictions
        if risk_score > 70:
            timeline = "6-12 months"
        elif risk_score > 50:
            timeline = "1-2 years"
        elif risk_score > 30:
            timeline = "2-5 years"
        else:
            timeline = "5+ years"
        
        return {
            'risk_score': risk_score,
            'timeline_to_regulation': timeline,
            'risk_level': self._get_risk_level(risk_score),
            'mitigation_priority': 'High' if risk_score > 50 else 'Medium' if risk_score > 30 else 'Low'
        }
    
    def _get_risk_level(self, score: float) -> str:
        """Convert risk score to level."""
        if score >= 70:
            return "Critical"
        elif score >= 50:
            return "High"
        elif score >= 30:
            return "Medium"
        elif score >= 10:
            return "Low"
        else:
            return "Minimal"


def main():
    """Example usage of ethical assessment."""
    assessor = EthicalAssessment()
    
    print("=== Ethical Assessment Example ===\n")
    
    # Define stakeholder impacts for a hypothetical decision
    impacts = [
        StakeholderImpact(
            group=StakeholderGroup.CUSTOMERS,
            immediate_impact=2,
            long_term_impact=3,
            reversible=True,
            has_consent=True,
            power_differential='low',
            affected_count=10000
        ),
        StakeholderImpact(
            group=StakeholderGroup.EMPLOYEES,
            immediate_impact=-1,
            long_term_impact=1,
            reversible=True,
            has_consent=False,
            power_differential='high',
            affected_count=500
        ),
        StakeholderImpact(
            group=StakeholderGroup.ENVIRONMENT,
            immediate_impact=-2,
            long_term_impact=-3,
            reversible=False,
            has_consent=False,
            power_differential='high',
            affected_count=1000000
        ),
        StakeholderImpact(
            group=StakeholderGroup.SHAREHOLDERS,
            immediate_impact=4,
            long_term_impact=2,
            reversible=True,
            has_consent=True,
            power_differential='low',
            affected_count=5000
        )
    ]
    
    # Analyze stakeholder impacts
    stakeholder_analysis = assessor.calculate_stakeholder_score(impacts)
    
    print("Stakeholder Impact Analysis:")
    print(f"  Weighted Score: {stakeholder_analysis['weighted_score']:.2f}")
    print(f"  Benefit/Harm Ratio: {stakeholder_analysis['benefit_harm_ratio']:.2f}")
    print(f"  Most Benefited: {stakeholder_analysis['most_benefited']}")
    print(f"  Most Harmed: {stakeholder_analysis['most_harmed']}")
    print(f"  Total Affected: {stakeholder_analysis['total_affected']:,}\n")
    
    # Apply ethical frameworks
    context = {
        'total_benefit': stakeholder_analysis['total_benefit'],
        'total_harm': stakeholder_analysis['total_harm'],
        'affected_count': stakeholder_analysis['total_affected'],
        'respects_autonomy': False,
        'truthful': True,
        'universalizable': False,
        'benefits_least_advantaged': False,
        'demonstrates_integrity': 3
    }
    
    ethical_analysis = assessor.apply_ethical_frameworks("Launch new product", context)
    
    print("Ethical Framework Analysis:")
    print(f"  Utilitarian Score: {ethical_analysis['utilitarian']['score']:.1f}")
    print(f"  Deontological Score: {ethical_analysis['deontological']['score']:.1f}")
    print(f"  Virtue Ethics Score: {ethical_analysis['virtue_ethics']['score']:.1f}")
    print(f"  Rawlsian Score: {ethical_analysis['rawlsian']['score']:.1f}")
    print(f"  Overall: {ethical_analysis['recommendation']}\n")
    
    # Calculate trust impact
    trust = assessor.calculate_trust_score(
        credibility=7,
        reliability=8,
        intimacy=6,
        self_orientation=4
    )
    print(f"Trust Score: {trust:.1f}/100\n")
    
    # Project reputation impact
    reputation = assessor.project_reputation_impact(
        current_reputation=75,
        decision_impact=-20,
        years=5
    )
    
    print("Reputation Trajectory:")
    for point in reputation['trajectory']:
        print(f"  Year {point['year']}: {point['reputation']}")
    
    if reputation['recovery_years']:
        print(f"  Recovery in: {reputation['recovery_years']} years\n")
    else:
        print("  Full recovery not achieved in projection period\n")
    
    # Analyze regulatory risk
    reg_risk = assessor.analyze_regulatory_risk(
        current_compliance=True,
        public_sentiment=0.6,
        incident_rate=2,
        lobby_strength=0.3
    )
    
    print("Regulatory Risk:")
    print(f"  Risk Score: {reg_risk['risk_score']:.1f}")
    print(f"  Risk Level: {reg_risk['risk_level']}")
    print(f"  Expected Regulation: {reg_risk['timeline_to_regulation']}")


if __name__ == "__main__":
    main()