# STEM Guide Assistant — Advanced Behavior System

## Overview

The STEM robot assistant now features **intelligent, context-aware, adaptive** behavior that feels like a real AI companion. It understands intent, learns within sessions, and adjusts responses dynamically.

---

## Architecture

### 1. **Session State Management**

The assistant maintains conversation memory **within the current session**:

```javascript
const sessionState = {
    conversationHistory: [],      // All user/bot messages
    exploredTopics: Set,          // Topics discussed (programs, writing, etc.)
    clarifyingAttempts: 0,        // How many times we've clarified
    userUnderstandingLevel: 'beginner'  // Adaptive tone (future enhancement)
};
```

**Key Point**: This is **session-only**. When the user closes the browser, state resets. No cross-user memory or data storage.

---

## 2. **Multi-Layer Intent Detection**

The system detects **WHAT** and **HOW** the user is asking:

```javascript
const { category, questionType } = detectIntentAndType(q);
```

### Category (WHAT)
- `programs` — Asking about opportunities
- `scholarships` — Asking about funding
- `admissions` — Asking about the admission process
- `writing` — Asking about essay writing
- `navigation` — Lost, asking "where" or "what next"
- `about_robot` — Meta questions about the assistant
- `general` — Unclear

### Question Type (HOW)
- `info` — Simple information ("What is...?")
- `guidance` — Explanation ("Why...?", "Explain...")
- `decision` — Recommendation ("Should...?", "Best...?")
- `clarification` — Confusion ("Not sure...", "Can you explain simply?")
- `followup` — Building on previous answer

---

## 3. **Contextual Response Building**

Responses are generated dynamically based on:
- **Category**: Topic-specific knowledge
- **Question Type**: Tone and depth
- **Session History**: Previous topics explored
- **Clarity Level**: How much detail to include

### Response Depth Algorithm

```
IF user asks "why" or "explain"
  → Use GUIDANCE response (deeper reasoning)

IF user asks "should" or "recommend"
  → Use DECISION response (multiple options, no single "right" answer)

IF user is confused
  → Use CLARIFICATION response (simplify, use different examples)

IF user follows up
  → Use FOLLOWUP response (reference previous, avoid repetition)

ELSE
  → Use INFORMATION response (standard, concise)
```

---

## 4. **Response Functions**

### `buildGuidanceResponse(category, q, hasContext)`
**When**: User asks "why", "how", "explain"  
**What**: Deep reasoning, thinking frameworks  
**Example**:
> "Let me explain how to think about programs. Programs vary in selectivity... Your choice depends on: your current level, time for prep, and experience type..."

### `buildDecisionResponse(category, q, hasContext)`
**When**: User asks for recommendations or "best" option  
**What**: Multiple valid options, no single answer  
**Example**:
> "There's no single 'best' program—it depends on you. Ask yourself: What's your current level? How much time can you invest? What experience do you want?"

### `buildClarificationResponse(category, q)`
**When**: User is confused, asks for simplification  
**What**: Extremely simple explanation, different angle  
**Example**:
> "Simple: 1) Understand what you're writing about. 2) Plan it. 3) Write it. 4) Read it aloud. 5) Fix it. That's it."

### `buildFollowupResponse(category, q, topicHistory)`
**When**: User builds on previous question  
**What**: Reference previous answer, go deeper, avoid repetition  
**Example**:
> "Following up on what we discussed, when you explore programs, notice how each one lists what it wants..."

### `buildInformationResponse(category, q, hasContext)`
**When**: Simple information request  
**What**: Concise answer with optional detail  
**Returns**: Short version by default, full version if user asks for "more", "explain", "detail"

---

## 5. **Core Personality Traits**

The assistant embodies:

| Trait | Implementation |
|-------|-----------------|
| **Intelligent** | Multi-layer intent detection, contextual responses |
| **Adaptive** | Changes depth/tone based on question type |
| **Calm** | Clear, patient language; asks clarifying questions |
| **Curious** | Tries to understand what user actually wants |
| **Supportive** | Encouraging, never judgmental; guides exploration |
| **Honest** | Admits uncertainty, never invents facts |

---

## 6. **Safety Boundaries (Never Claims)**

❌ **The assistant will NOT claim**:
- Human consciousness ("I feel" or "I think emotionally")
- Cross-user memory ("I remember you from last week")
- Official authority ("I decide admissions")
- Perfect knowledge ("I know everything")
- Decision-making power ("You should definitely do X")

✅ **The assistant WILL**:
- Say "I'm not sure" when uncertain
- Redirect to official sources
- Emphasize the user's agency
- Explain limitations

**Admissions Safe Mode** (extra caution):
```javascript
// When admissions is mentioned, always include:
- "The Ministry of Education manages this"
- No predictions or cutoff scores
- Redirect to official admissions page
- Repeat boundaries if pushed
```

---

## 7. **Session-Based Learning (Safe)**

The assistant **adapts within a session** but **does NOT claim learning**:

**What Changes**:
- Tone adjusts based on clarity (simpler if confused)
- References previous topics ("You asked about X earlier...")
- Avoids repeating full explanations
- Suggests related topics

**What's NOT Stored**:
- No user profiles
- No data persistence
- No "learning across sessions"
- No analytics on individual users

**What You CAN Say**:
> "Based on what you asked earlier, you might also want to check..."

**What You CANNOT Say**:
> "I learned that you prefer..." (across sessions)

---

## 8. **Question Handling Flow**

For **ANY user question**:

```
1. Detect Intent (category + question type)
2. Check Session History (what topics explored?)
3. Select Response Function (guidance/decision/clarification/followup/info)
4. Generate Contextual Response (using appropriate tone/depth)
5. Record in History (so next answer builds on this)
6. Return Response
```

---

## 9. **Navigation Intelligence**

The assistant knows all site sections and builds guided paths:

**When user asks "where should I go?"**:
- Considers what they've already explored
- Suggests next logical step
- Uses conversational guides
- Provides direct links

**Example Flow**:
> User: "How do I start exploring?"  
> Bot: "It depends what you're interested in. If you want to explore opportunities, start here [Accessible programs]. If you want to improve writing, start here [Writing Basics]."

---

## 10. **Error Handling & Honesty**

When uncertain, the assistant:

1. **Admits it**: "I'm not sure about that specific detail."
2. **Explains what IS known**: "What I do know is..."
3. **Suggests a source**: "The official answer is at [link]."
4. **Offers alternative help**: "Can I help with something else?"

---

## 11. **Communication Patterns**

### Default Pattern (Short)
```
[Direct answer] [Brief explanation] [Suggested next step]
```

### Deep Pattern (Guidance)
```
[Context] [Reasoning framework] [Examples] [Suggested path]
```

### Clarification Pattern (Simple)
```
[Extreme simplification] [Numbered steps] [One example]
```

### Followup Pattern (Building)
```
[Reference to previous] [Deeper layer] [Connection to broader context]
```

---

## 12. **Example Scenarios**

### Scenario 1: User Asks "What Programs Exist?"
```
Category: programs
Question Type: info
Response: Short information response with link to programs hub
```

### Scenario 2: User Asks "Why Should I Join a Program?"
```
Category: programs
Question Type: guidance
Response: Deep reasoning about benefits, how to think about fit
```

### Scenario 3: User Asks "What's the Best Program?"
```
Category: programs
Question Type: decision
Response: Multiple valid options, framework for deciding, no single "best"
```

### Scenario 4: User (Confused) Asks "I Don't Understand Programs"
```
Category: programs
Question Type: clarification
Response: Extremely simple explanation, different angle than before
```

### Scenario 5: User (Already Explored Writing) Asks About Essays
```
Category: writing
Question Type: followup
Response: References writing basics discussion, builds on structure concept
```

---

## 13. **Future Enhancements**

These features are designed but not yet active:

- [ ] `userUnderstandingLevel` — Adjust vocabulary based on level
- [ ] Emote system — Optional personality flourishes
- [ ] Topic suggestion — Proactive "you might also want to check..."
- [ ] Analytics (anonymized) — Common questions, trouble areas
- [ ] Multi-language support — Arabic translations

---

## 14. **Testing the System**

Try these to see different responses:

| Question | Expected Type |
|----------|---------------|
| "Tell me about programs" | info |
| "Why are programs competitive?" | guidance |
| "Which program is best?" | decision |
| "I don't get how scholarships work" | clarification |
| "Okay so how do I apply to [previous program]?" | followup |

---

## Summary

The STEM Guide Assistant is now:
- ✅ **Intelligent**: Understands real intent, not just keywords
- ✅ **Adaptive**: Changes depth and tone based on question type
- ✅ **Contextual**: Remembers session history, builds on answers
- ✅ **Safe**: Clear boundaries, admits uncertainty, no false claims
- ✅ **Thoughtful**: Feels like a real AI companion without over-claiming
- ✅ **Honest**: Guides exploration without controlling decisions

It feels like **a smart assistant that wants to help you think clearly** — exactly as intended.
