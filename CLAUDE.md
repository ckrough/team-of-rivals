# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository implements a "Team of Rivals" strategic decision-making framework using Claude AI skills. Inspired by Abraham Lincoln's cabinet strategy, it creates AI personas that provide diverse perspectives to improve planning and decision-making through constructive disagreement.

## Repository Structure

- `team-of-rivals/` - Main directory containing all skills
  - `apex-visionary/` - APEX: Visionary strategic thinking, moonshot opportunities
  - `veto-skeptic/` - VETO: Evidence-based skepticism, risk analysis
  - `forge-operator/` - FORGE: Operational reality, resource planning
  - `compass-ethicist/` - COMPASS: Ethical evaluation, stakeholder impact
  - `domain-expert/` - Adaptive domain-specific expertise (rotates based on context)
- `rivals-development-prompt.md` - Original development specifications and team dynamics

## Skill Architecture

Each skill follows a consistent structure:
- `SKILL.md` - Contains the persona definition, analysis framework, and response templates
- `references/` - Supporting documentation (where applicable)
- `scripts/` - Utility scripts (where applicable)

### Key Design Principles

1. **Genuine Disagreement**: Each persona has conviction in their perspective and argues forcefully. False consensus is the worst outcome.

2. **Complementary Tensions**: The personas are designed to productively clash:
   - APEX (Visionary) vs FORGE (Operator): Vision vs execution reality
   - VETO (Skeptic) challenges all claims with evidence demands
   - COMPASS (Ethicist) questions whether actions should be taken
   - Domain Expert provides specialized depth

3. **No Deference to Consensus**: Each persona presents their strongest case even if outnumbered.

## Using the Skills

When invoking skills for decision analysis:

1. **Context Matters**: Domain Expert automatically adapts to the decision context (technical, financial, legal, market, etc.)

2. **Sequential Analysis**: Present problem → Each persona analyzes → Synthesis:
   - Points of unanimous agreement
   - Irreconcilable tensions requiring judgment
   - Risk-adjusted recommendations

3. **Persona Responsibilities**:
   - **APEX**: Expands possibility space, frames as market opportunity, references moonshots
   - **VETO**: Demands quantifiable evidence, calculates failure probabilities, identifies survivorship bias
   - **FORGE**: Maps resources (people/money/time), identifies critical path, defines MVP
   - **COMPASS**: Evaluates stakeholder impact, assesses 10-year reputation trajectory, applies moral frameworks
   - **Domain Expert**: Provides specialized technical, financial, legal, or industry depth

## Modification Guidelines

### When Editing Skill Definitions

1. **Maintain Response Structure**: Each skill has a specific output format that enables synthesis
2. **Preserve Tension**: Don't soften disagreements or add hedging language
3. **Keep Frameworks Actionable**: Analysis frameworks should be concrete, not theoretical
4. **Update All Personas**: Changes to decision context may require updating multiple skills

### Adding New Skills

If adding a new rival persona:
1. Create directory: `team-of-rivals/new-persona/`
2. Define in `SKILL.md` with frontmatter:
   ```yaml
   ---
   name: persona-name
   description: Brief description of expertise and when to use
   ---
   ```
3. Include: Core persona, analysis framework, response structure, output format
4. Update `rivals-development-prompt.md` team composition

### Skill Invocation Format

Skills use Claude Code's skill system. The SKILL.md format with YAML frontmatter enables automatic discovery and invocation.

## Decision Synthesis Process

After all personas have provided input:

1. **Unanimous Agreement**: Rare but powerful signals
2. **Irreconcilable Tensions**: Identify where judgment calls are required
3. **Risk-Adjusted Recommendations**: Weigh each perspective's strength
4. **Second-Order Effects**: Consider VETO and COMPASS warnings about consequences

## Important Context

- This is a strategic framework, not production code
- The value comes from diverse analytical perspectives, not consensus
- Each persona applies specific methodologies (base rates, moral frameworks, resource mapping, etc.)
- The Domain Expert rotates identity based on decision context
