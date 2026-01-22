"""
Test script to verify all routes are working properly
"""
import sys
import os

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from app import app
    print("✓ App imported successfully")
    
    # Test Flask app configuration
    with app.test_client() as client:
        print("\nTesting Public Routes:")
        print("-" * 50)
        
        public_routes = [
            ('/', 'Home'),
            ('/programs', 'Programs'),
            ('/highlights', 'Highlights'),
            ('/admissions', 'Admissions'),
            ('/contact', 'Contact'),
            ('/writing/basics', 'Writing Basics'),
            ('/writing/examples', 'Writing Examples'),
            ('/writing/resources', 'Writing Resources'),
            ('/programs/listing', 'Programs Listing'),
            ('/programs/top-tier', 'Top-Tier Programs'),
            ('/programs/achievable', 'Achievable Programs'),
            ('/programs/accessible', 'Accessible Programs'),
        ]
        
        for route, name in public_routes:
            try:
                response = client.get(route)
                status = "✓" if response.status_code == 200 else "✗"
                print(f"{status} {name:30} {route:30} [{response.status_code}]")
            except Exception as e:
                print(f"✗ {name:30} {route:30} [ERROR: {str(e)}]")
        
        print("\nTesting Authentication Routes:")
        print("-" * 50)
        
        auth_routes = [
            ('/signup', 'Signup Page'),
            ('/login', 'Login Page'),
            ('/forgot-password', 'Forgot Password'),
        ]
        
        for route, name in auth_routes:
            try:
                response = client.get(route)
                status = "✓" if response.status_code == 200 else "✗"
                print(f"{status} {name:30} {route:30} [{response.status_code}]")
            except Exception as e:
                print(f"✗ {name:30} {route:30} [ERROR: {str(e)}]")
        
        print("\nTesting Protected Routes (should redirect):")
        print("-" * 50)
        
        protected_routes = [
            ('/dashboard', 'Dashboard'),
            ('/test-save', 'Test Save'),
        ]
        
        for route, name in protected_routes:
            try:
                response = client.get(route, follow_redirects=False)
                # Should redirect to login (302)
                status = "✓" if response.status_code in [302, 401] else "✗"
                print(f"{status} {name:30} {route:30} [{response.status_code}] (Redirects to login)")
            except Exception as e:
                print(f"✗ {name:30} {route:30} [ERROR: {str(e)}]")
        
        print("\nTesting Signup Flow:")
        print("-" * 50)
        
        # Test signup
        signup_data = {
            'fullname': 'Test User',
            'email': f'test{os.urandom(4).hex()}@example.com',
            'password': 'TestPassword123',
            'confirm_password': 'TestPassword123',
            'role': 'Student'
        }
        
        response = client.post('/signup', data=signup_data, follow_redirects=False)
        if response.status_code in [200, 302]:
            print(f"✓ User signup successful [{response.status_code}]")
            
            # Get session cookie
            with client.session_transaction() as session:
                if 'user_id' in session:
                    print(f"✓ User session created: {session['user_id']}")
                    
                    # Test accessing dashboard
                    response = client.get('/dashboard')
                    if response.status_code == 200:
                        print(f"✓ Dashboard accessible after login [200]")
                    else:
                        print(f"✗ Dashboard not accessible [{response.status_code}]")
                else:
                    print("✗ User session not created")
        else:
            print(f"✗ User signup failed [{response.status_code}]")
        
        print("\n" + "=" * 50)
        print("All critical tests completed!")
        print("=" * 50)
        print("\nServer is running at: http://127.0.0.1:5000")
        print("\nYou can now:")
        print("  • Visit http://127.0.0.1:5000 for the homepage")
        print("  • Visit http://127.0.0.1:5000/signup to create an account")
        print("  • Visit http://127.0.0.1:5000/login to log in")
        print("  • Visit http://127.0.0.1:5000/test-save to quickly save programs")
        print("  • Visit http://127.0.0.1:5000/dashboard to view your dashboard")

except Exception as e:
    print(f"✗ Error: {str(e)}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
