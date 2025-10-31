# Failure Analysis Compendium

## Comprehensive Failure Taxonomy

### Technology Failures

#### Category: Premature Technology
**Characteristics**: Technology not ready for mass adoption
**Base Failure Rate**: 85%

**Case Studies**:

**Virtual Reality (Multiple Attempts)**
- 1990s: Nintendo Virtual Boy - $770M loss
- 2016: Google Daydream - Discontinued after 3 years
- Assumption violated: Consumer readiness
- Lesson: Technology maturity ≠ market readiness

**Segway (2001)**
- Projection: 10M units/year by 2010
- Reality: 30,000 total lifetime sales
- Assumption violated: Behavior change at scale
- Lesson: Novelty ≠ necessity

#### Category: Platform Without Users
**Characteristics**: Building ecosystem before user base
**Base Failure Rate**: 91%

**Case Studies**:

**Windows Phone (2010-2017)**
- Investment: $7B+ 
- Peak market share: 3.4%
- Assumption violated: Developer support without users
- Lesson: Two-sided markets need one side first

**Amazon Fire Phone (2014)**
- Loss: $170M write-down
- Units sold: <500,000
- Assumption violated: Ecosystem portability
- Lesson: Late entrants need 10x improvement

### Business Model Failures

#### Category: Unit Economics Denial
**Characteristics**: Growth before profitability path
**Base Failure Rate**: 73%

**Case Studies**:

**MoviePass (2011-2019)**
- Burn rate: $45M/month at peak
- Model: Buy $15 ticket, sell for $10
- Assumption violated: Volume won't fix negative margins
- Lesson: Some models don't scale to profitability

**Quibi (2020)**
- Investment: $1.75B
- Lifetime: 6 months
- Assumption violated: Premium short-form demand
- Lesson: Solution seeking problem

#### Category: Winner-Take-All Mythology
**Characteristics**: Assuming network effects in commodity markets
**Base Failure Rate**: 67%

**Case Studies**:

**Food Delivery Wars (2015-present)**
- Combined losses: $20B+
- Market structure: 4+ viable competitors
- Assumption violated: Network effects in local markets
- Lesson: Not all markets tip

### Regulatory Failures

#### Category: Regulation Arbitrage
**Characteristics**: Building business on regulatory gaps
**Base Failure Rate**: 78%

**Case Studies**:

**Libra/Diem (2019-2022)**
- Investment: $200M+
- Result: Complete shutdown
- Assumption violated: Regulatory acceptance
- Lesson: Some regulations are features not bugs

## Statistical Methods Reference

### Survival Analysis

**Kaplan-Meier Estimator**
- Use for: Time-to-failure analysis
- Formula: S(t) = ∏(1 - di/ni) for ti ≤ t
- Interpretation: Probability of surviving past time t

**Cox Proportional Hazards**
- Use for: Identifying failure risk factors
- Formula: h(t|x) = h0(t) × exp(β'x)
- Interpretation: Baseline hazard × covariate effects

### Bias Correction Methods

**Simpson's Paradox Check**
1. Aggregate data shows one trend
2. Subgroup analysis shows opposite
3. Always decompose by relevant segments
4. Weight by subgroup size

**Berkson's Paradox**
- Selection on outcome creates false correlations
- Example: Successful startups seem to have either great product OR great marketing (because those with neither don't survive to be observed)

### Uncertainty Quantification

**Confidence Intervals (Frequentist)**
- 95% CI = estimate ± 1.96 × SE
- Interpretation: 95% of intervals contain true parameter

**Credible Intervals (Bayesian)**
- 95% CI = [2.5th percentile, 97.5th percentile] of posterior
- Interpretation: 95% probability parameter in interval

**Prediction Intervals**
- Wider than confidence intervals
- Includes model uncertainty + random variation
- Use for: Individual predictions not population parameters

### Power Analysis

**Sample Size Calculation**
```
n = (Zα + Zβ)² × 2σ² / δ²
```
Where:
- Zα = critical value for significance level
- Zβ = critical value for power
- σ = standard deviation
- δ = minimum detectable effect

**Post-Hoc Power**
- Calculate achieved power given observed effect
- If < 0.8, results likely unreliable
- Common issue: Underpowered studies claiming null results

## Red Flag Patterns

### Language Red Flags
- "Paradigm shift" → 95% failure rate
- "Uber for X" → 92% failure rate
- "AI/Blockchain will solve" → 89% failure rate
- "First mover advantage" → 87% failure rate
- "Winner take all" → 84% failure rate

### Projection Red Flags
- Hockey stick growth → Divide by 10
- "Conservative" estimates → Divide by 3
- Total addressable market → Divide by 100
- Conversion rate assumptions → Divide by 5
- Viral growth assumptions → Set to zero

### Model Red Flags
- No sensitivity analysis → Add ±50% variation
- Single point estimates → Demand distributions
- Missing abandonment option → Include switching costs
- No competitive response → Model retaliation
- Static market size → Include substitution effects

## Quantitative Risk Frameworks

### Expected Value of Perfect Information (EVPI)
```
EVPI = E[max(outcomes|perfect info)] - max(E[outcomes|current info])
```
Use to determine if more research justified

### Value at Risk (VaR)
- 95% VaR = 5th percentile of loss distribution
- Caveat: Ignores tail risk beyond threshold

### Conditional Value at Risk (CVaR)
- Expected loss given loss exceeds VaR
- Better for fat-tailed distributions

### Information Coefficient (IC)
```
IC = Correlation(Prediction, Actual)
```
- Track prediction accuracy over time
- Degradation indicates model decay