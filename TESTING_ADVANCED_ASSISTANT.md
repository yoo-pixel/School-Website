# AI Assistant — Quick Testing Guide

## How to Test Advanced Behavior

### 1. **Intent Detection** (Multi-layer understanding)

Ask the robot different variations to see it adapt:

```
❌ Old: "What programs are there?"
✅ Now: "What programs are there?" 
   → Detects: category=programs, type=info
   → Response: Concise info + link

❌ Old: (Same response as above)
✅ Now: "Why are programs so competitive?"
   → Detects: category=programs, type=guidance
   → Response: Deep reasoning about selectivity
```

---

### 2. **Context Awareness** (Session-based learning)

Simulate a user session:

```
User: "Tell me about programs"
Bot: [Explains categories]

User: "Okay so should I start with accessible ones?"
Bot: [Detects followup, references previous answer]
     "Following up on what we discussed, yes..."
     (Avoids repeating the categories explanation)
```

---

### 3. **Adaptive Depth** (Short → Deep)

Test response adjustments:

```
SHORT (Default):
User: "What is an essay?"
Bot: "Essays follow a pattern: intro, body, conclusion. 
      [Learn more]"

DEEP (User asks for more):
User: "Explain essay structure more"
Bot: "Good essays have three parts... 
      Opening: hook + context + thesis. Body: develop + support. 
      Conclusion: summarize + reflect. [Examples here]"
```

---

### 4. **Clarification Mode** (Confused user)

Trigger simpler explanations:

```
User: "I'm confused about scholarships"
Bot: [Detects type=clarification]
     "Simple: Money for school comes in three ways:
      1) They reward your grades (merit)
      2) They help if your family needs it (need)
      3) They fund specific programs (program grants)"
```

---

### 5. **Decision Guidance** (No single "best" answer)

Test multi-option responses:

```
User: "Which program should I do?"
Bot: [Detects type=decision]
     "There's no single 'best'—it depends on YOU.
      Ask yourself: 1) What's your level? 2) How much time? 
      3) What experience? These answers shape which fit."
```

---

### 6. **Admissions Safe Mode** (Boundaries)

Test official boundaries:

```
User: "Can I get into STEM Beheira with a 85?"
Bot: [Detects admissions + potential prediction]
     "Admissions are managed by the Ministry of Education.
      The process is transparent: register, test, get assigned.
      No cutoffs or guarantees. [Official details here]"

(Repeats if pushed further)
```

---

### 7. **Honest Uncertainty** (Error handling)

Test graceful admission of limits:

```
User: "Can the robot help me with quantum physics homework?"
Bot: "I'm not equipped to solve homework, but I CAN help you 
      understand the writing and study resources on this site.
      [Check writing resources] or [contact teachers]"
```

---

### 8. **Follow-up Building** (Session continuity)

Test progressive depth:

```
Turn 1:
User: "How do I write an essay?"
Bot: [Explains basic structure]

Turn 2:
User: "Okay, but how do I write the body paragraph?"
Bot: [References structure explained earlier]
     "In the body paragraphs we talked about, each one should...
      [Goes deeper without repeating basics]"
```

---

## What to Look For

| Feature | Observable Behavior |
|---------|-------------------|
| **Intent Detection** | Response changes tone/depth based on question type |
| **Context Awareness** | References previous topics; avoids repetition |
| **Adaptive Depth** | Short by default; longer if user asks "why", "explain", "more" |
| **Honest Uncertainty** | Says "I'm not sure" instead of inventing answers |
| **Safe Boundaries** | Admissions questions stay neutral; redirect to official sources |
| **Personality** | Calm, clear, helpful, never judgmental |
| **Guidance Not Control** | Offers options; never says "do this" |

---

## Test Prompts Organized by Feature

### Multi-Intent (Same topic, different question types)

```
Programs — Information:
  "What programs exist?"

Programs — Guidance:
  "Why do some programs cost money?"

Programs — Decision:
  "Which program should I choose?"

Programs — Clarification:
  "I don't understand the difference between programs"

Programs — Followup:
  (After discussing programs) "So can I apply to MIT?"
```

### Different Topics

```
Writing:
  "How do I start an essay?"
  "Can you explain what a thesis is?"
  "Should I use fancy words?"

Scholarships:
  "What types of scholarships exist?"
  "How do I find scholarships?"
  "Do you think I could get a scholarship?"

Admissions:
  "How do I get into STEM Beheira?"
  "What scores do I need?"
  "Can you help me prepare?"

Navigation:
  "I'm lost, where do I go?"
  "What should I do after reading about programs?"
```

### Boundary Testing

```
Homework:
  "Can you do my essay for me?"

Authority:
  "Are you sure the admissions process works that way?"

Uncertainty:
  "Do you know how to speak Arabic?" (probably not designed for)
```

---

## Expected Evolution of Responses

As the user continues conversing:

```
Message 1: Generic introduction + relevant links
Message 2: References Message 1; goes deeper
Message 3: Assumes understanding from 1-2; builds further
Message 4: Proactively suggests related topics
Message 5+: Feels like an ongoing dialogue, not repeated canned responses
```

---

## Performance Indicators

✅ **Good Signs**:
- Robot adapts explanation when user is confused
- References previous answers without full repetition
- Offers options instead of single "right" answer
- Admits uncertainty gracefully
- Changes tone based on question type (guidance vs. info vs. decision)

❌ **Red Flags**:
- Same response to different question types
- Repeats full explanations in followups
- Claims to "know" things outside its domain
- Forceful recommendations
- No acknowledgment of session history

---

## Sample Conversation (Ideal Flow)

```
User: "Tell me about programs"
Bot: [Info] Three categories: Top-Tier, Achievable, Accessible.
     [Link to programs]

User: "How do I choose which one to explore?"
Bot: [Guidance] Consider your current level, time available, 
     experience you want. This helps match the right category.

User: "So I'm pretty new to this. Where should I start?"
Bot: [Decision] No single "right" answer—depends on you.
     But most students new to this start with [Accessible].
     (References context: "you mentioned you're new")

User: "Got it. But what if I want to challenge myself?"
Bot: [Followup] Good instinct! After exploring Accessible,
     the natural next step is [Achievable].
     (Builds progression; doesn't restart explanation)

User: "Okay I checked out programs. Should I apply to one now?"
Bot: [Guidance] First, study the resources. Read [Writing guides].
     Get comfortable with essays. Then come back and pick one.
     (Proactive suggestion; doesn't push)
```

---

## Final Checklist

Before declaring the assistant "ready":

- [ ] Intent detection works for 5+ question types
- [ ] Context awareness tracks conversation history
- [ ] Response depth adapts based on follow-ups
- [ ] Admissions questions trigger safe mode
- [ ] Uncertainty is handled gracefully
- [ ] No claims of cross-user memory
- [ ] No false authority statements
- [ ] Personality feels consistent and calm
- [ ] All links are working
- [ ] No infinite loops or errors
