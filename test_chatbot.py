#!/usr/bin/env python3
"""
Test script for INGRES ChatBot MVP
Tests various query types and validates responses
"""

import requests
import json
import time
from typing import Dict, Any

# Configuration
API_BASE_URL = "http://localhost:5000/api"

# Test queries
TEST_QUERIES = [
    {
        "query": "What is the groundwater status of Delhi?",
        "expected_intent": "groundwater_status",
        "description": "Testing location-based groundwater status query"
    },
    {
        "query": "Show me critical areas",
        "expected_intent": "critical_areas",
        "description": "Testing critical areas identification"
    },
    {
        "query": "Which areas are safe?",
        "expected_intent": "safe_areas",
        "description": "Testing safe areas identification"
    },
    {
        "query": "What is the water level in Gurugram?",
        "expected_intent": "water_level",
        "description": "Testing water level query"
    },
    {
        "query": "Show historical data",
        "expected_intent": "historical",
        "description": "Testing historical data retrieval"
    },
    {
        "query": "What is the annual recharge rate?",
        "expected_intent": "recharge",
        "description": "Testing recharge data query"
    },
    {
        "query": "How much groundwater is being extracted?",
        "expected_intent": "extraction",
        "description": "Testing extraction data query"
    },
    {
        "query": "Help",
        "expected_intent": "help",
        "description": "Testing help functionality"
    }
]

def test_health_check() -> bool:
    """Test if the API is running"""
    try:
        response = requests.get(f"{API_BASE_URL}/health")
        if response.status_code == 200:
            data = response.json()
            print("✅ Health Check: API is running")
            print(f"   Service: {data.get('service', 'Unknown')}")
            return True
        else:
            print("❌ Health Check Failed: API returned status", response.status_code)
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Health Check Failed: Cannot connect to API at", API_BASE_URL)
        print("   Make sure the backend server is running (python backend/app.py)")
        return False
    except Exception as e:
        print(f"❌ Health Check Failed: {str(e)}")
        return False

def test_chat_query(query: str, expected_intent: str = None) -> Dict[str, Any]:
    """Test a single chat query"""
    try:
        response = requests.post(
            f"{API_BASE_URL}/chat",
            json={"message": query},
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            data = response.json()
            
            # Check if expected intent matches
            if expected_intent and data.get('intent') != expected_intent:
                print(f"⚠️  Intent mismatch: Expected '{expected_intent}', got '{data.get('intent')}'")
            
            return {
                "success": True,
                "data": data,
                "status_code": response.status_code
            }
        else:
            return {
                "success": False,
                "error": f"API returned status {response.status_code}",
                "status_code": response.status_code
            }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

def test_database_stats() -> bool:
    """Test database statistics endpoint"""
    try:
        response = requests.get(f"{API_BASE_URL}/stats")
        if response.status_code == 200:
            data = response.json()
            print("\n📊 Database Statistics:")
            
            if 'coverage' in data:
                coverage = data['coverage']
                print(f"   States: {coverage.get('states', 0)}")
                print(f"   Districts: {coverage.get('districts', 0)}")
                print(f"   Blocks: {coverage.get('blocks', 0)}")
            
            if 'category_distribution' in data:
                print("\n   Category Distribution:")
                for category, count in data['category_distribution'].items():
                    print(f"   - {category}: {count} blocks")
            
            return True
        else:
            print("❌ Stats Check Failed: API returned status", response.status_code)
            return False
    except Exception as e:
        print(f"❌ Stats Check Failed: {str(e)}")
        return False

def run_tests():
    """Run all tests"""
    print("=" * 60)
    print("         INGRES ChatBot MVP - Test Suite")
    print("=" * 60)
    print()
    
    # Step 1: Health Check
    print("Step 1: Testing API Health...")
    if not test_health_check():
        print("\n⚠️  Cannot proceed with tests. Please start the backend server.")
        return
    
    print()
    time.sleep(1)
    
    # Step 2: Database Stats
    print("Step 2: Testing Database Statistics...")
    test_database_stats()
    
    print()
    time.sleep(1)
    
    # Step 3: Test Queries
    print("Step 3: Testing Chat Queries...")
    print("-" * 60)
    
    passed = 0
    failed = 0
    
    for i, test in enumerate(TEST_QUERIES, 1):
        print(f"\nTest {i}/{len(TEST_QUERIES)}: {test['description']}")
        print(f"Query: \"{test['query']}\"")
        
        result = test_chat_query(test['query'], test.get('expected_intent'))
        
        if result['success']:
            data = result['data']
            print(f"✅ Success!")
            print(f"   Intent: {data.get('intent', 'Unknown')}")
            
            # Show entities if present
            entities = data.get('entities', {})
            if entities:
                print(f"   Entities: {json.dumps(entities, indent=6)}")
            
            # Show a snippet of the response
            response_text = data.get('response', '')
            if response_text:
                # Get first line of response
                first_line = response_text.split('\n')[0][:100]
                print(f"   Response: {first_line}...")
            
            passed += 1
        else:
            print(f"❌ Failed: {result.get('error', 'Unknown error')}")
            failed += 1
        
        time.sleep(0.5)  # Small delay between requests
    
    # Summary
    print("\n" + "=" * 60)
    print("                    TEST SUMMARY")
    print("=" * 60)
    print(f"Total Tests: {len(TEST_QUERIES)}")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print(f"Success Rate: {(passed/len(TEST_QUERIES)*100):.1f}%")
    
    if passed == len(TEST_QUERIES):
        print("\n🎉 All tests passed successfully!")
    elif failed == 0:
        print("\n✨ Tests completed with warnings.")
    else:
        print(f"\n⚠️  {failed} test(s) failed. Please check the implementation.")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    try:
        run_tests()
    except KeyboardInterrupt:
        print("\n\n⚠️  Tests interrupted by user.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
    
    print("\nPress Enter to exit...")
    input()
