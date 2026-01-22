# 🤖 STEM Guide Assistant — Feature Reference Card

## Quick Facts

| Feature | Status | Implementation |
|---------|--------|-----------------|
| Intent Detection | ✅ Active | Multi-layer (category + type) |
| Session Memory | ✅ Active | Conversation history + explored topics |
| Adaptive Depth | ✅ Active | 5 response builders by question type |
| Context Awareness | ✅ Active | References previous answers |
| Safe Boundaries | ✅ Active | No false claims, admissions safe mode |
| Error Handling | ✅ Active | Graceful admission of uncertainty |
| Navigation Help | ✅ Active | Knows all site sections |
| Personality | ✅ Active | Calm, clear, helpful, honest |

---

## The 5 Response Builders

### 1️⃣ **buildGuidanceResponse()**
**When**: User asks "why", "how", "explain"  
**Tone**: Educational, reasoning-focused  
**Depth**: Deep — explains frameworks  
**Example**:
```
User: "Why are some programs competitive?"
Bot: "Let me explain. Programs vary in selectivity...
     Your choice depends on: level, time, experience..."
```

### 2️⃣ **buildDecisionResponse()**
**When**: User asks "should", "recommend", "best"  
**Tone**: Balanced, non-prescriptive  
**Depth**: Options, not commands  
**Example**:
```
User: "Which program should I do?"
Bot: "There's no single 'best'—it depends on YOU.
     Ask yourself: level? time? experience?"
```

### 3️⃣ **buildClarificationResponse()**
**When**: User is confused or asks for simplification  
**Tone**: Patient, step-by-step  
**Depth**: Minimal — only essentials  
**Example**:
```
User: "I'm confused about scholarships"
Bot: "Simple: 1) Merit-based (grades), 
     2) Need-based (money help),
     3) Program-specific (for certain fields)"
```

### 4️⃣ **buildFollowupResponse()**
**When**: User builds on previous question  
**Tone**: Connected, progressive  
**Depth**: Assumes prior context  
**Example**:
```
User: (earlier) "Tell me about programs"
User: (now) "How do I choose?"
Bot: "Following up on what we discussed...
     When you explore, notice how each lists..."
```

### 5️⃣ **buildInformationResponse()**
**When**: Simple information request  
**Tone**: Clear, concise  
**Depth**: Short by default, full if asked  
**Example**:
```
User: "What is an essay?"
Bot: "Essays: intro → body → conclusion. [Learn more]"

User: "Tell me more"
Bot: "Opening: hook+context+thesis. Body: ideas+support..."
```

---

## Intent Detection Matrix

### Category Detection

```
"program"  OR "opportunity" OR "summer" OR "ai" OR "stem"
  → category: "programs"

"scholarship" OR "financial" OR "fund" OR "money"
  → category: "scholarships"

"admission" OR "apply" OR "exam" OR "eligible" OR "get in"
  → category: "admissions"

"writing" OR "essay" OR "english" OR "grammar" OR "improve"
  → category: "writing"

"help" OR "lost" OR "confused"
  → category: "navigation"

"robot" OR "assistant" OR "you" OR "can you"
  → category: "about_robot"
```

### Question Type Detection

```
"why" OR "how" OR "explain" OR "understand"
  → questionType: "guidance"

"should" OR "recommend" OR "best" OR "what do i"
  → questionType: "decision"

"confused" OR "unclear" OR "not sure" OR "mean"
  → questionType: "clarification"

(detected as followup to previous question)
  → questionType: "followup"

(default)
  → questionType: "info"
```

---

## Session State Structure

```javascript
sessionState = {
  conversationHistory: [
    { role: 'user', text: 'Tell me about programs' },
    { role: 'bot', text: 'Programs come in three levels...' },
    { role: 'user', text: 'Why are they competitive?' },
    { role: 'bot', text: 'Let me explain...' }
  ],
  
  exploredTopics: Set ['programs', 'writing'],
  
  clarifyingAttempts: 0,
  
  userUnderstandingLevel: 'beginner'  // for future use
}
```

---

## Response Generation Flow

```
Input: "Why do programs cost money?"

↓ Detect Intent
  category: "programs"
  questionType: "guidance"

↓ Check Context
  exploredTopics includes "programs"? YES → hasContext = true

↓ Select Builder
  questionType === "guidance" → buildGuidanceResponse()

↓ Generate Response
  Include: context from previous questions
  Tone: Explanatory, deep
  Pattern: Answer → Explain → Next Step

↓ Record History
  conversationHistory.push({ role: 'user', ... })
  conversationHistory.push({ role: 'bot', ... })

↓ Return to User
```

---

## Safety Boundaries Checklist

### ✅ The Assistant CAN Say

```
"I'm not sure about that specific detail, but..."
"The official answer is here: [link]"
"Let me explain how to think about this..."
"Here are several valid options, depending on..."
"Can you tell me more about what you're trying..."
"Based on what you asked earlier..."
"That's outside what I'm designed to help with..."
```

### ❌ The Assistant MUST NOT Say

```
"I learned from previous users that..."
"You should definitely do this..."
"I'm certain the answer is..."
"The admission requirement is..."
"I'll solve your homework for you..."
"I know exactly what's best for you..."
```

### 🔐 Admissions Safe Mode

When `category === 'admissions'`:
- ✅ Include: "Ministry of Education"
- ✅ Include: "transparent" and "fair"
- ✅ Include: Link to official page
- ❌ Exclude: Predictions or cutoffs
- ❌ Exclude: "You should"
- ❌ Exclude: Guarantees or promises

---

## Testing Checklist

### ✅ Features to Verify

- [ ] Intent detection changes response by question type
- [ ] Context awareness references previous topics
- [ ] Clarity adjusts based on follow-ups
- [ ] Admissions questions stay neutral
- [ ] Uncertainty is handled gracefully
- [ ] All links are working and correct
- [ ] No repeated explanations in followups
- [ ] Personality is consistent
- [ ] No false claims or over-statements

### Sample Test Prompts

```
Program Questions (different types):
□ "What programs are there?" (info)
□ "Why are programs competitive?" (guidance)
□ "Which program is best?" (decision)
□ "I'm confused about programs" (clarification)

Writing Questions:
□ "How do I write an essay?" (info)
□ "Can you explain thesis statements?" (guidance)

Admissions Questions:
□ "How do I get into STEM Beheira?" (info/safe mode)
□ "What scores do I need?" (safe mode - no predictions)

Navigation:
□ "I'm lost, help me" (navigation)
□ "What should I do next?" (guidance)

Meta:
□ "What can you do?" (about_robot)
□ "Can you do my homework?" (boundary)
```

---

## Response Patterns

### Pattern 1: Information (Default - Short)
```
[Answer] [Brief Explanation] [Link]

Example:
"Programs come in three levels: Top-Tier, Achievable, Accessible.
Explore them here to find what fits you."
```

### Pattern 2: Guidance (Deep - Reasoning)
```
[Context] [Framework] [Examples] [Path]

Example:
"Let me explain. Programs vary in selectivity...
Your choice depends on: 1) level, 2) time, 3) experience.
Think about each and it will guide you..."
```

### Pattern 3: Clarification (Simple - Steps)
```
[Extreme Simplification] [Numbered Steps]

Example:
"Simple: 1) Read. 2) Plan. 3) Write. 4) Fix. That's it."
```

### Pattern 4: Followup (Building - References)
```
[Reference Previous] [Go Deeper] [Connect]

Example:
"Following up on what we discussed about programs...
The next step is to explore one that matches your level..."
```

---

## Architecture at a Glance

```
ASSISTANT ENGINE

┌─ Session State ─────────────────┐
│ • Conversation History          │
│ • Explored Topics (no cross-    │
│   user memory)                  │
│ • Understanding Level (future)  │
└─────────────────────────────────┘
         ↓
┌─ Intent Detection ──────────────┐
│ WHAT: Category (programs, etc)  │
│ HOW: Type (info/guidance/etc)   │
└─────────────────────────────────┘
         ↓
┌─ Response Builder Selection ────┐
│ • buildGuidanceResponse()       │
│ • buildDecisionResponse()       │
│ • buildClarificationResponse()  │
│ • buildFollowupResponse()       │
│ • buildInformationResponse()    │
└─────────────────────────────────┘
         ↓
┌─ Generate Response ─────────────┐
│ • Context-aware               │
│ • Safe boundaries             │
│ • Personality-consistent      │
│ • Adaptive depth              │
└─────────────────────────────────┘
         ↓
┌─ Record & Return ───────────────┐
│ • Update session state         │
│ • Record in history            │
│ • Return to user               │
└─────────────────────────────────┘
```

---

## Key Advantages Over Basic System

| Aspect | Basic | Advanced |
|--------|-------|----------|
| Intent | Keywords | Category + Type |
| Memory | None | Session history |
| Depth | Same | Adaptive |
| Clarity | One approach | Tailored |
| Followups | Repetitive | Progressive |
| Safety | Generic | Explicit boundaries |
| Personality | Static | Context-aware |

---

## Files & Locations

```
Implementation:
  static/app.js (lines 1430-1764)
  - initAssistant() IIFE
  - sessionState object
  - All response builders
  - Intent detection system

Documentation:
  ASSISTANT_BEHAVIOR_GUIDE.md
  - Full system architecture
  - All functions documented
  - Code examples
  - Future roadmap
  
  TESTING_ADVANCED_ASSISTANT.md
  - Test scenarios
  - Expected behaviors
  - Red flags
  - Example flows
  
  ASSISTANT_IMPLEMENTATION_SUMMARY.md
  - This file's parent
  - Complete overview
  - Implementation checklist
  - Status report
```

---

## Status: ✅ READY FOR TESTING

All features implemented, syntax validated, documentation complete.

Next: Deploy and test in browser using TESTING_ADVANCED_ASSISTANT.md
