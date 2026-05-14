"""
=============================================================
  CHAPTER 9 REVIEWER: Program Validation, Testing & Code Review
  Batangas State University — ACP Final Exam Reviewer
=============================================================
  TOPICS COVERED:
    1. Flowchart & Pseudocode — role in testing/validation
    2. Debugging — types of errors
       (Syntax, Runtime, Semantic)
    3. System Validation
       — Verification vs Validation
    4. User Acceptance Testing (UAT)
    5. Functional Testing
    6. Non-Functional Testing
    7. Software Testing — why it matters
    8. System Testing (Black Box vs White Box)
    9. Manual Testing — Black Box & White Box
   10. Automation Testing
   11. Test Case Table Format
   12. Code Review — types & steps

  HOW TO USE:
    Run this file in IDLE, VS Code, or any Python interpreter.
    All output is printed to the console.
    Interactive quizzes are included at the end.
=============================================================
"""

print("=" * 62)
print("  CHAPTER 9 REVIEWER: Validation, Testing & Code Review")
print("=" * 62)


# ─────────────────────────────────────────────
# SECTION 1: FLOWCHART & PSEUDOCODE
# Key ideas:
#   Flowchart  → DIAGRAM using standardized symbols
#                visualizes logic BEFORE coding
#   Pseudocode → human-readable, plain language version of code
#                blueprint for test cases
#   Both help:
#     ✔ Visualize logic before coding
#     ✔ Detect logical errors early
#     ✔ Verify if algorithm follows correct steps
#     ✔ Make debugging easier
# ─────────────────────────────────────────────
print("\n── SECTION 1: Flowchart & Pseudocode ──────────────────")
print("""
  FLOWCHART
    Definition: A DIAGRAM that visually represents steps
                in a program using standardized symbols.
    Role in testing & validation:
      ✔ Helps VISUALIZE logic before coding
      ✔ Makes it easier to detect LOGICAL ERRORS early
      ✔ Used to VERIFY if the algorithm follows correct steps

  PSEUDOCODE
    Definition: Structured, HUMAN-READABLE version of code
                written in plain language.
    Role in testing & validation:
      ✔ Helps VERIFY logic before actual coding
      ✔ Acts as a BLUEPRINT for test cases
      ✔ Makes DEBUGGING easier since logic is clear

  Example Pseudocode — Check if a number is positive:
    START
      INPUT number
      IF number > 0 THEN
        PRINT "Positive"
      ELSE
        PRINT "Not Positive"
      END IF
    END
""")

# Python implementation of that pseudocode
def check_positive(number):
    if number > 0:
        return "Positive"
    else:
        return "Not Positive"

print("  Python from pseudocode above:")
for n in [5, -3, 0]:
    print(f"    check_positive({n:>3}) → {check_positive(n)}")


# ─────────────────────────────────────────────
# SECTION 2: DEBUGGING — TYPES OF ERRORS
# Key ideas:
#   Syntax Error  → caught by interpreter BEFORE running
#                   e.g. missing colon, wrong indentation
#   Runtime Error → occurs WHILE program is running
#                   e.g. division by zero, infinite recursion
#   Semantic Error→ program RUNS but gives WRONG results
#                   e.g. wrong formula, wrong condition
# ─────────────────────────────────────────────
print("\n── SECTION 2: Debugging — Types of Errors ─────────────")
print("""
  ┌─────────────────┬───────────────────────────────────────┐
  │   Error Type    │   Description & Example               │
  ├─────────────────┼───────────────────────────────────────┤
  │ SYNTAX ERROR    │ Caught by interpreter during           │
  │                 │ translation (before running).          │
  │                 │ Example: SyntaxError: invalid syntax   │
  │                 │   → missing colon after if/def         │
  │                 │   → wrong indentation                  │
  ├─────────────────┼───────────────────────────────────────┤
  │ RUNTIME ERROR   │ Produced during program execution.     │
  │                 │ Example: ZeroDivisionError             │
  │                 │          RecursionError (infinite loop) │
  │                 │          NameError, TypeError          │
  ├─────────────────┼───────────────────────────────────────┤
  │ SEMANTIC ERROR  │ Program RUNS without crashing but      │
  │                 │ produces WRONG results.                │
  │                 │ Example: Using + instead of *          │
  │                 │          Wrong formula in calculation  │
  └─────────────────┴───────────────────────────────────────┘
""")

# Demonstrating semantic error detection
print("  Semantic Error Example — Wrong area formula:")

def area_wrong(l, w):
    return l + w       # BUG: should be l * w (semantic error)

def area_correct(l, w):
    return l * w       # CORRECT

print(f"    area_wrong(5, 3)   = {area_wrong(5, 3)}  ← Wrong! (used +)")
print(f"    area_correct(5, 3) = {area_correct(5, 3)}  ← Correct (used *)")

# Demonstrating safe runtime error handling
print("\n  Runtime Error Example — Handled with try/except:")
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "ERROR: Cannot divide by zero (Runtime Error)"

print(f"    safe_divide(10, 2) = {safe_divide(10, 2)}")
print(f"    safe_divide(10, 0) = {safe_divide(10, 0)}")


# ─────────────────────────────────────────────
# SECTION 3: SYSTEM VALIDATION
# Key ideas:
#   Validation  → "Am I building the RIGHT product?"
#                  Does software meet USER NEEDS?
#   Verification→ "Am I building the product RIGHT?"
#                  Is it built correctly per specs?
#   System Validation: test in REAL conditions,
#                       from the USER's point of view
# ─────────────────────────────────────────────
print("\n── SECTION 3: System Validation ───────────────────────")
print("""
  SYSTEM VALIDATION
    Definition: Evaluating a COMPLETE software system to
                determine if it meets the USER'S NEEDS and
                intended purpose.

    Key question: "Am I building the RIGHT product?"

  VERIFICATION vs VALIDATION (common exam topic!)
  ┌──────────────────┬──────────────────────────────────────┐
  │   VERIFICATION   │   VALIDATION                         │
  ├──────────────────┼──────────────────────────────────────┤
  │ Am I building    │ Am I building the RIGHT product?     │
  │ the product      │                                      │
  │ RIGHT?           │                                      │
  ├──────────────────┼──────────────────────────────────────┤
  │ Unit Test        │ Customer Acceptance Test              │
  │ Integration Test │ Usability Test                        │
  │ Automated Test   │                                       │
  ├──────────────────┼──────────────────────────────────────┤
  │ Tests code       │ Tests against user requirements       │
  └──────────────────┴──────────────────────────────────────┘

  Tests that belong to BOTH (overlap):
    Regression Testing, System Testing, Beta Testing
""")


# ─────────────────────────────────────────────
# SECTION 4: USER ACCEPTANCE TESTING (UAT)
# Key ideas:
#   Actual USERS or CLIENTS test the system
#   Confirms it meets their needs in REAL-WORLD use
#   What happens in UAT:
#     → Users test real-life scenarios
#     → Check if workflows are correct and easy to use
#     → Report issues or confirm everything works
#   System PASSES UAT when all scenarios match expectations
# ─────────────────────────────────────────────
print("\n── SECTION 4: User Acceptance Testing (UAT) ───────────")
print("""
  UAT — User Acceptance Testing
    Who:  ACTUAL USERS or CLIENTS (not developers)
    What: Test real-life scenarios in the system
    Goal: Confirm the system works as expected in real-world use

  What happens in UAT:
    1. Users test real scenarios (login, place order, generate report)
    2. Check if workflows are CORRECT and EASY TO USE
    3. Report issues or CONFIRM everything works properly

  Example — Online Shopping App UAT checklist:
    ✔ Can users add items to cart?
    ✔ Is checkout working correctly?
    ✔ Are payments processed properly?
    → If ALL match expectations → System PASSES UAT
""")


# ─────────────────────────────────────────────
# SECTION 5: FUNCTIONAL TESTING
# Key ideas:
#   Checks if system works according to SPECIFIED REQUIREMENTS
#   Based on functional requirements / specifications
#   Validates user actions and system RESPONSES
#   Focuses on OUTPUTS produced by INPUTS
#   Does NOT consider internal code structure
#   Common areas tested:
#     UI functions, APIs, Data processing,
#     Business logic, Database interactions
# ─────────────────────────────────────────────
print("\n── SECTION 5: Functional Testing ──────────────────────")
print("""
  FUNCTIONAL TESTING
    Checks whether a system works according to its
    SPECIFIED REQUIREMENTS.

    What happens:
      ✔ Based on functional requirements/specifications
      ✔ Validates USER actions and SYSTEM responses
      ✔ Focuses on OUTPUTS produced by INPUTS
      ✔ Does NOT consider internal code structure

  Common areas tested:
    • User interface functions
    • APIs and system responses
    • Data processing
    • Business logic (calculations, workflows)
    • Database interactions

  Example — Login System Functional Test:
    Input: correct username + password → Expected: dashboard opens
    Input: wrong password              → Expected: error message shown
    Input: empty fields                → Expected: validation message shown
""")

# Simulating functional test in Python
print("  Python simulation of Login functional test:")

def login(username, password):
    """Simulates a login system."""
    VALID_USER = "user123"
    VALID_PASS = "pass@123"
    if not username or not password:
        return "❌ Validation: Fields cannot be empty"
    elif username == VALID_USER and password == VALID_PASS:
        return "✅ Login successful — Dashboard opens"
    else:
        return "❌ Error: Incorrect username or password"

test_cases = [
    ("user123", "pass@123"),
    ("user123", "wrongpass"),
    ("",        ""),
]
for user, pwd in test_cases:
    result = login(user, pwd)
    print(f"    login({repr(user)}, {repr(pwd)}) → {result}")


# ─────────────────────────────────────────────
# SECTION 6: NON-FUNCTIONAL TESTING
# Key ideas:
#   Tests NON-FUNCTIONAL aspects of software
#   (NOT about what it does, but HOW WELL it does it)
#   Non-Functional Testing Parameters:
#     Security, Availability, Efficiency, Integrity
#     Reliability, Survivability, Usability, Flexibility
#     Scalability, Reusability, Interoperability, Portability
# ─────────────────────────────────────────────
print("\n── SECTION 6: Non-Functional Testing ──────────────────")
print("""
  NON-FUNCTIONAL TESTING
    Tests HOW WELL the system works (not just WHAT it does).
    Tests aspects that functional testing does NOT cover.

  Non-Functional Testing Parameters:
  ┌──────────────────┬──────────────────────────────────────┐
  │   Security       │  Is the system safe from attacks?    │
  │   Availability   │  Is the system always accessible?    │
  │   Efficiency     │  Does it use resources well?         │
  │   Integrity      │  Is data accurate and consistent?    │
  │   Reliability    │  Does it perform consistently?       │
  │   Usability      │  Is it easy to use?                  │
  │   Scalability    │  Can it handle growth in users/data? │
  │   Portability    │  Does it work on different platforms? │
  │   Flexibility    │  Can it adapt to new requirements?   │
  │   Reusability    │  Can parts be reused elsewhere?      │
  └──────────────────┴──────────────────────────────────────┘
""")


# ─────────────────────────────────────────────
# SECTION 7: SOFTWARE TESTING — WHY IT MATTERS
# Key ideas:
#   Software testing = method to check software meets
#                      requirements and is defect-free
#   Purpose: identify ERRORS, GAPS, or MISSING REQUIREMENTS
#   Important because: bugs can be EXPENSIVE or DANGEROUS
#                      (monetary and human loss)
# ─────────────────────────────────────────────
print("\n── SECTION 7: Software Testing — Why It Matters ───────")
print("""
  SOFTWARE TESTING
    Definition: Method to check whether actual software
                matches expected requirements and is DEFECT FREE.

    Purpose: Identify ERRORS, GAPS, or MISSING REQUIREMENTS
             in contrast to actual requirements.

    Why important?
      ✘ Software bugs can be EXPENSIVE
      ✘ Software bugs can be DANGEROUS
      ✘ History is full of examples of monetary and human loss
        caused by software bugs.
""")


# ─────────────────────────────────────────────
# SECTION 8: SYSTEM TESTING & BLACK/WHITE BOX
# Key ideas:
#   System Testing → validates COMPLETE & FULLY INTEGRATED
#                    software; evaluates end-to-end specs
#   Two categories:
#     Black Box → tests WITHOUT looking at internal code
#                 (tester only cares about input/output)
#     White Box → tests internal code, logic, structure
#                 (tester "looks inside the box")
#   System testing falls under BLACK BOX category
# ─────────────────────────────────────────────
print("\n── SECTION 8: System Testing — Black Box vs White Box ─")
print("""
  SYSTEM TESTING
    Validates the COMPLETE and FULLY INTEGRATED software.
    Purpose: evaluate END-TO-END system specifications.

  E2E (End-to-End) Specifications — Online Shopping Example:
    1. User logs in
    2. Searches for a product
    3. Adds item to cart
    4. Proceeds to checkout
    5. Enters payment details
    6. System processes payment
    7. Order confirmation is sent
    8. Inventory is updated
    9. Delivery is scheduled

  ┌──────────────────────┬──────────────────────────────────┐
  │   BLACK BOX TESTING  │   WHITE BOX TESTING              │
  ├──────────────────────┼──────────────────────────────────┤
  │ Does NOT look at     │ EXAMINES internal structure,      │
  │ internal code        │ code, and logic                   │
  │                      │                                  │
  │ Only cares about:    │ Testers "look INSIDE the box"    │
  │ Inputs & Outputs     │ Design tests based on code       │
  │                      │                                  │
  │ System test falls    │ Used for unit testing, code      │
  │ under this category  │ coverage analysis                │
  └──────────────────────┴──────────────────────────────────┘
""")

# White box example in Python
print("  White Box Testing simulation — branch coverage:")

def check_access(age):
    """
    White box: we TEST both branches of this if-else.
    Branch 1: age >= 18 → "granted"
    Branch 2: age <  18 → "denied"
    """
    if age >= 18:
        return "granted"
    else:
        return "denied"

# White box tester knows the code and tests BOTH branches
print(f"    check_access(20) → access {check_access(20)}  ← tests branch 1")
print(f"    check_access(15) → access {check_access(15)}   ← tests branch 2")
print("    (Both branches covered = 100% branch coverage)")


# ─────────────────────────────────────────────
# SECTION 9: MANUAL TESTING
# Key ideas:
#   Tests executed MANUALLY by a tester
#   No automated tools needed
#   Most primitive technique
#   Helps find CRITICAL BUGS
#   Does not require knowledge of any testing tool
# ─────────────────────────────────────────────
print("\n── SECTION 9: Manual Testing ───────────────────────────")
print("""
  MANUAL TESTING
    ✔ Tests executed MANUALLY by a human tester
    ✔ No automated tools required
    ✔ Most PRIMITIVE technique of all testing types
    ✔ Helps find CRITICAL bugs
    ✔ Does NOT require knowledge of any testing tool

  BLACK BOX (manual):
    Tester does NOT look at code.
    Only checks: Input → Action → Expected Output

    Example — Facebook Login:
      Step 1: Navigate to login page
      Step 2: Enter valid username
      Step 3: Enter valid password
      Step 4: Click Login
      Data: user1 / pass123
      Expected: User is redirected to dashboard

  WHITE BOX (manual):
    Tester READS the code and designs tests based on
    internal logic, ensuring all branches are covered.
""")


# ─────────────────────────────────────────────
# SECTION 10: AUTOMATION TESTING
# Key ideas:
#   Uses special AUTOMATED TESTING SOFTWARE TOOLS
#   Opposite of manual testing
#   Common tools: Selenium, QTP, JMeter, Loadrunner,
#                 TestLink, Quality Center (ALM)
# ─────────────────────────────────────────────
print("\n── SECTION 10: Automation Testing ─────────────────────")
print("""
  AUTOMATION TESTING
    Definition: Uses special AUTOMATED testing software tools
                to execute a test case suite.
    Opposite of: Manual Testing (human executes steps)

  Common Automation Testing Tools:
    • Selenium      → web browser automation
    • QTP           → QuickTest Professional
    • JMeter        → performance/load testing
    • Loadrunner    → load and performance testing
    • TestLink      → test management tool
    • Quality Center (ALM) → HP test management

  When to automate:
    ✔ Repetitive tests that run every build
    ✔ Regression tests
    ✔ Performance/load testing
    ✔ Large test suites that take too long manually
""")


# ─────────────────────────────────────────────
# SECTION 11: TEST CASE TABLE FORMAT
# Key ideas:
#   Test Case Table = structured format in SQA
#   Used to document, organize, execute, and track test cases
#   Fields:
#     1. Test Case ID    → unique identifier
#     2. Test Scenario   → short description of what is tested
#     3. Preconditions   → conditions before executing test
#     4. Test Steps      → step-by-step actions
#     5. Test Data       → input values
#     6. Expected Result → what should happen if correct
#     7. Actual Result   → what actually happened
#     8. Status          → Pass / Fail
#     9. Remarks         → extra notes / bug ID
# ─────────────────────────────────────────────
print("\n── SECTION 11: Test Case Table Format ─────────────────")
print("""
  TEST CASE TABLE
    A STRUCTURED FORMAT used in Software Quality Assurance (SQA)
    to document and organize test cases clearly so they can be
    executed, tracked, and reviewed easily.

  Fields:
    1. Test Case ID   → unique identifier (e.g. TC_001)
    2. Test Scenario  → short description of what is tested
    3. Preconditions  → must be true BEFORE executing test
    4. Test Steps     → step-by-step actions to perform
    5. Test Data      → input values used in the test
    6. Expected Result→ what should happen if system is correct
    7. Actual Result  → what actually happened during testing
    8. Status         → Pass / Fail / Blocked
    9. Remarks        → extra notes, bug IDs, comments
""")

# Simulated Test Case Table using Python
test_cases_table = [
    {
        "TC_ID":    "TC_001",
        "Scenario": "Valid Login",
        "Precond":  "User registered",
        "Steps":    "Enter credentials → Click login",
        "Data":     "user123 / pass@123",
        "Expected": "Dashboard opens",
        "Actual":   "Dashboard opened",
        "Status":   "✅ PASS",
    },
    {
        "TC_ID":    "TC_002",
        "Scenario": "Wrong Password",
        "Precond":  "User registered",
        "Steps":    "Enter wrong password → Click login",
        "Data":     "user123 / wrongpass",
        "Expected": "Error message shown",
        "Actual":   "Error message shown",
        "Status":   "✅ PASS",
    },
    {
        "TC_ID":    "TC_003",
        "Scenario": "Empty Fields",
        "Precond":  "On login page",
        "Steps":    "Leave fields empty → Click login",
        "Data":     "(empty) / (empty)",
        "Expected": "Validation message shown",
        "Actual":   "No validation shown",
        "Status":   "❌ FAIL",
    },
]

print("  Sample Test Case Table — System Login:")
print(f"  {'TC ID':<8} {'Scenario':<18} {'Data':<22} {'Status'}")
print("  " + "-" * 60)
for tc in test_cases_table:
    print(f"  {tc['TC_ID']:<8} {tc['Scenario']:<18} {tc['Data']:<22} {tc['Status']}")


# ─────────────────────────────────────────────
# SECTION 12: CODE REVIEW
# Key ideas:
#   Developers examine SOURCE CODE written by ANOTHER developer
#   BEFORE it is merged into the main codebase
#   Improves: quality, security, maintainability
#
#   Types of Code Review:
#     1. Peer Review     → most common; developers review each other
#     2. Senior Review   → senior dev / tech lead reviews critical code
#     3. Automated Review→ tools check formatting, bugs, vulnerabilities
#
#   Steps in Peer Review:
#     1.  Receive code (Pull Request / Merge Request via GitHub)
#     2.  Understand the requirement & acceptance criteria
#     3.  High-level scan — check overall design approach
#     4.  Check logic and correctness
#     5.  Review code quality — follows coding standards?
#     6.  Check performance — heavy ops inside loops?
#     7.  Check security — input validation, safe handling
#     8.  Check testing — covers positive + negative cases?
#     9.  Add clear comments — suggest improvements
#     10. Approve or request changes
#          Approve         → code is good to merge
#          Request changes → issues must be fixed
#          Comment only    → minor suggestions
# ─────────────────────────────────────────────
print("\n── SECTION 12: Code Review ─────────────────────────────")
print("""
  CODE REVIEW
    Process where developers EXAMINE source code written by
    ANOTHER developer BEFORE merging into the main codebase.
    Most important practice in real-world software development.
    Benefits: improves QUALITY, SECURITY, and MAINTAINABILITY.

  Types of Code Review:
    1. PEER REVIEW     → most common; devs review each other's code
    2. SENIOR REVIEW   → tech lead reviews critical/complex code
    3. AUTOMATED REVIEW→ tools check formatting, bugs, vulnerabilities

  Steps in Peer Review (10 steps):
    1.  Receive the code (Pull Request / Merge Request)
        → via GitHub / GitLab / Bitbucket
    2.  Understand the requirement
        → know expected behavior & acceptance criteria
    3.  High-level scan first
        → check overall design approach
    4.  Check logic and correctness
        → does the code solve the problem correctly?
    5.  Review code quality
        → follows coding standards?
    6.  Check performance (if relevant)
        → heavy operations inside loops?
    7.  Check security
        → input validation? safe handling of user input?
    8.  Check testing
        → do tests cover POSITIVE + NEGATIVE cases?
    9.  Add clear comments
        → suggest improvements constructively
    10. Approve or request changes:
          ✅ Approve         → code is GOOD to merge
          🔁 Request changes → issues MUST be fixed
          💬 Comment only   → minor suggestions

  Code Review Checklist (quick reference):
""")

checklist = [
    ("Logic correct?",           "Does the code solve the problem as intended?"),
    ("Follows standards?",        "Naming, formatting, indentation consistent?"),
    ("Input validated?",          "Are user inputs checked before use?"),
    ("Error handling?",           "Are exceptions handled gracefully?"),
    ("Performance OK?",           "No unnecessary loops or expensive operations?"),
    ("Tests included?",           "Positive AND negative test cases present?"),
    ("Security checked?",         "No SQL injection, no exposed credentials?"),
    ("Readable/maintainable?",    "Would another dev understand this easily?"),
]
for item, desc in checklist:
    print(f"    ☐ {item:<25} {desc}")


# ─────────────────────────────────────────────
# QUICK REFERENCE CHEAT SHEET
# ─────────────────────────────────────────────
print("""
╔══════════════════════════════════════════════════════════════╗
║   CHAPTER 9 CHEAT SHEET — Validation, Testing & Review       ║
╠══════════════════════════════════════════════════════════════╣
║  ERROR TYPES                                                 ║
║   Syntax  → caught before running (typos, missing colons)    ║
║   Runtime → occurs while running (divide by zero, recursion) ║
║   Semantic→ runs but gives wrong result (wrong formula)      ║
╠══════════════════════════════════════════════════════════════╣
║  TESTING TYPES                                               ║
║   UAT           → users verify real-world scenarios          ║
║   Functional    → inputs/outputs match specifications        ║
║   Non-Functional→ performance, security, usability, etc.     ║
║   System        → full end-to-end integration test           ║
║   Black Box     → test without looking at code               ║
║   White Box     → test with knowledge of code/logic          ║
║   Manual        → human executes test steps                  ║
║   Automation    → tools execute tests (Selenium, JMeter)     ║
╠══════════════════════════════════════════════════════════════╣
║  VERIFICATION vs VALIDATION                                  ║
║   Verification → "Am I building the product RIGHT?"          ║
║   Validation   → "Am I building the RIGHT product?"          ║
╠══════════════════════════════════════════════════════════════╣
║  TEST CASE FIELDS (9 fields)                                 ║
║   TC ID → Scenario → Preconditions → Test Steps →            ║
║   Test Data → Expected → Actual → Status → Remarks           ║
╠══════════════════════════════════════════════════════════════╣
║  CODE REVIEW TYPES                                           ║
║   Peer → Senior → Automated                                  ║
║  CODE REVIEW OUTCOME                                         ║
║   Approve / Request Changes / Comment Only                   ║
╚══════════════════════════════════════════════════════════════╝
""")


# ─────────────────────────────────────────────
# BONUS: MINI QUIZ (interactive)
# ─────────────────────────────────────────────
def run_quiz():
    questions = [
        {
            "q": "What type of error is caught BEFORE the program runs?",
            "choices": ["A. Runtime Error", "B. Semantic Error",
                        "C. Syntax Error", "D. Logic Error"],
            "answer": "C",
            "explain": "Syntax errors are caught by the interpreter during translation."
        },
        {
            "q": "What does UAT stand for?",
            "choices": ["A. Unified Acceptance Test", "B. User Acceptance Testing",
                        "C. Unit Automated Testing", "D. User Application Test"],
            "answer": "B",
            "explain": "UAT = User Acceptance Testing — done by actual users."
        },
        {
            "q": "Black Box Testing means the tester:",
            "choices": ["A. Reads the source code", "B. Writes unit tests",
                        "C. Does NOT look at the internal code",
                        "D. Uses automated tools only"],
            "answer": "C",
            "explain": "Black Box testers only care about inputs, actions, and outputs."
        },
        {
            "q": "Which is NOT a field in a Test Case Table?",
            "choices": ["A. Test Case ID", "B. Expected Result",
                        "C. Developer Name", "D. Actual Result"],
            "answer": "C",
            "explain": "Developer Name is not a standard test case table field."
        },
        {
            "q": "In Code Review, 'Request Changes' means:",
            "choices": ["A. Minor suggestions only", "B. Code is good to merge",
                        "C. Issues MUST be fixed before merging",
                        "D. The code is deleted"],
            "answer": "C",
            "explain": "Request Changes means issues must be fixed before the code can merge."
        },
    ]

    print("\n── BONUS: MINI QUIZ ────────────────────────────────────")
    print("  Answer each question (type the letter A, B, C, or D)\n")

    score = 0
    for i, q in enumerate(questions, 1):
        print(f"  Q{i}: {q['q']}")
        for choice in q['choices']:
            print(f"       {choice}")
        answer = input("  Your answer: ").strip().upper()
        if answer == q['answer']:
            print(f"  ✅ Correct!\n")
            score += 1
        else:
            print(f"  ❌ Incorrect. Answer: {q['answer']}")
            print(f"     Explanation: {q['explain']}\n")

    print(f"  ── Quiz Result: {score}/{len(questions)} ──")
    if score == len(questions):
        print("  🏆 Perfect score! You're ready for the exam!")
    elif score >= 3:
        print("  👍 Good job! Review the topics you missed.")
    else:
        print("  📚 Keep studying! Re-read the sections above.")


# Ask if student wants to take the quiz
print("\n" + "─" * 62)
try:
    take_quiz = input("  Would you like to take the mini quiz? (y/n): ").strip().lower()
    if take_quiz == "y":
        run_quiz()
    else:
        print("  Skipping quiz. Good luck on your exam!")
except (EOFError, KeyboardInterrupt):
    print("  (Quiz skipped)")

print("\n✅ Chapter 9 Reviewer Complete! Good luck on your exam!")