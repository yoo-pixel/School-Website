"""
Test script for enhanced ChatGPT-level assistant

Tests the semantic understanding, context awareness, and conversational flexibility
"""

import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def test_assistant():
    """Test the enhanced assistant with various conversational patterns"""
    
    session = requests.Session()
    
    test_cases = [
        # ===== TEST 1: Natural Conversation Flow =====
        {
            "name": "Basic Question - Programs",
            "message": "what programs are available?",
            "expected_contains": ["programs", "level", "accessible"],
            "description": "User asks about programs - should get informative response"
        },
        
        # ===== TEST 2: Vague Follow-up with Context Inference =====
        {
            "name": "Vague Follow-up Question",
            "message": "how do i get into one?",
            "expected_contains": ["get", "apply", "register"],
            "description": "After discussing programs, 'one' should be inferred as programs"
        },
        
        # ===== TEST 3: Guidance Request =====
        {
            "name": "Guidance - How to Think",
            "message": "why should i choose one program over another?",
            "expected_contains": ["depends", "choose", "goals"],
            "description": "Why question should trigger guidance response"
        },
        
        # ===== TEST 4: Decision Support =====
        {
            "name": "Decision Question",
            "message": "which program should i pick?",
            "expected_contains": ["depends", "situation", "goals"],
            "description": "Should get decision-support response"
        },
        
        # ===== TEST 5: Writing Help =====
        {
            "name": "Writing Question",
            "message": "how do i write a good essay?",
            "expected_contains": ["structure", "intro", "conclusion"],
            "description": "Writing question should get educational response"
        },
        
        # ===== TEST 6: Scholarships Question =====
        {
            "name": "Scholarships",
            "message": "tell me about scholarships",
            "expected_contains": ["scholarship", "merit", "funding"],
            "description": "Should explain scholarship types"
        },
        
        # ===== TEST 7: Admissions Process =====
        {
            "name": "Admissions Question",
            "message": "how does the admissions process work?",
            "expected_contains": ["ministry", "exam", "process"],
            "description": "Should explain Ministry process"
        },
        
        # ===== TEST 8: Incomplete Question =====
        {
            "name": "Incomplete/Vague Question",
            "message": "that sounds good",
            "expected_contains": ["help", "explore", "let me"],
            "description": "Vague statement should get contextual guidance"
        },
        
        # ===== TEST 9: Question with Typos/Variations =====
        {
            "name": "Variations of 'program'",
            "message": "what opportunities are there?",
            "expected_contains": ["program", "opportunities", "explore"],
            "description": "Should recognize 'opportunities' as program-related"
        },
        
        # ===== TEST 10: Clarification Request =====
        {
            "name": "I don't understand",
            "message": "i dont get it can you explain simpler",
            "expected_contains": ["simple", "think", "ladder"],
            "description": "Should provide simplified explanation"
        },
    ]
    
    print("\n" + "="*70)
    print("ENHANCED ASSISTANT - CONVERSATIONAL INTELLIGENCE TEST")
    print("="*70 + "\n")
    
    passed = 0
    failed = 0
    
    for i, test in enumerate(test_cases, 1):
        print(f"TEST {i}: {test['name']}")
        print(f"Message: '{test['message']}'")
        print(f"Description: {test['description']}")
        
        try:
            # Send message to assistant
            response = session.get(
                f"{BASE_URL}/api/assistant",
                params={"message": test['message']}
            )
            
            if response.status_code == 200:
                data = response.json()
                assistant_reply = data.get('response', '')
                
                print(f"\nAssistant Response:\n{assistant_reply[:200]}...\n")
                
                # Check if expected content is in response
                expected_found = any(
                    keyword.lower() in assistant_reply.lower() 
                    for keyword in test['expected_contains']
                )
                
                if expected_found:
                    print("✅ PASSED - Response contains expected keywords")
                    passed += 1
                else:
                    print("❌ FAILED - Response missing expected content")
                    print(f"Expected to find: {test['expected_contains']}")
                    failed += 1
            else:
                print(f"❌ FAILED - HTTP Error {response.status_code}")
                failed += 1
                
        except Exception as e:
            print(f"❌ FAILED - Exception: {e}")
            failed += 1
        
        print("-" * 70 + "\n")
    
    # Summary
    print("="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Total:  {passed + failed}")
    print(f"Success Rate: {(passed/(passed+failed)*100):.1f}%")
    print("="*70 + "\n")
    
    if failed == 0:
        print("🎉 All tests passed! Enhanced assistant is working great!")
    else:
        print(f"⚠️ {failed} test(s) failed. Review the assistant responses above.")

if __name__ == "__main__":
    print("\nStarting Enhanced Assistant Test Suite...")
    print("Make sure Flask server is running on http://127.0.0.1:5000\n")
    
    try:
        test_assistant()
    except requests.exceptions.ConnectionError:
        print("ERROR: Cannot connect to Flask server at http://127.0.0.1:5000")
        print("Make sure the Flask app is running: python app.py")
    except Exception as e:
        print(f"ERROR: {e}")
