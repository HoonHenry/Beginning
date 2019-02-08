#include <gtest/gest.h>
#include <string>

//TEST(FizzBuzzTest, doesPass)
//{
//	ASSERT_TRUE(true);
//}

//string fizzBuzz(int value)
//{
//	return "";
//}

string fizzBuzz(int value)
{
	if (3 == value)
		return "Fizz";
	return to_string(value);
}

void checkFizzBuzz(int value, std::string expectedResult)
{
	string result = fizzBuzz(value);
	ASSERT_STREQ(expectedResult.c_str, result.c_str());
}

//TEST(FizzBuzzTests, canCallFizzBuzz)
//{
//	string result = fizzBuzz(1);
//}

TEST(FizzBuzzTests, returnsWithPassedIn)
{
	string result = fizzBuzz(1);
	ASSERT_STREQ("1", result.c_str());
}

TEST(FizzBuzzTests, returnWith2PassedIn)
{
	string result = fizzBuzz(2);
	ASSERT_STREQ("2", result.c_str());
}

TEST(FizzBuzzTests, returnWith3PassedIn)
{
	checkFizzBuzz(3, "Fizz");
}