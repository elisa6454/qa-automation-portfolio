# Bug Reports

## BUG-001: No minimum length limit for password

**Steps to reproduce**

1. Go to the signup page
2. Enter a 1-character password (example: "1")
3. Fill in the other required fields correctly
4. Submit the account

**Expected result**: The system should show a validation error if the password is too short (example: minimum 8 characters).

**Actual result**: The account is created successfully with no length check on the password.

**Severity**: Medium
**Priority**: High

---

## BUG-002: Weak email format validation

**Steps to reproduce**

1. Go to the signup page
2. Enter an email with only "@" and no proper domain format (example: "a@b")
3. Submit the account

**Expected result**: The system should reject emails that don't follow a standard format (example: name@domain.com).

**Actual result**: The email "a@b" is accepted as valid.

**Severity**: Low
**Priority**: Low

---

## BUG-003: Search fails with 2 or more leading spaces

**Steps to reproduce**

1. Go to the Products page
2. Search for " Dress" (two spaces before the keyword)
3. Check the results

**Expected result**: Leading/trailing spaces should be trimmed automatically, and the search should return the same results as searching "Dress".

**Actual result**: With one leading space, the search works fine. With two or more leading spaces, no results are shown.

**Severity**: Low
**Priority**: Low

---

## BUG-004: Search results include unrelated products

**Steps to reproduce**

1. Go to the Products page
2. Search for "Dr"
3. Check the product names in the results

**Expected result**: Results should only include products that have "Dr" somewhere in the product name.

**Actual result**: Some products without "Dr" in the name also appear in the results — for example, a product named "Sleeves Top and Short - Blue & Pink" was included, likely because its category is "Dress". It looks like the search also matches by category, not only by product name.

**Severity**: Low
**Priority**: Low

---

## BUG-005: No format validation for mobile number

**Steps to reproduce**

1. Go to the signup page
2. Enter "0" (a single digit) in the Mobile Number field
3. Fill in the other required fields correctly
4. Submit the account

**Expected result**: The system should validate the mobile number format (example: minimum digit count, numbers only).

**Actual result**: The account is created successfully even with just "0" as the mobile number.

**Severity**: Low
**Priority**: Low

---

## BUG-006: API returns 200 instead of documented error status codes

**Steps to reproduce**

1. Send a POST request to `/api/verifyLogin` without the email parameter
2. Send a POST request to `/api/verifyLogin` with invalid email/password

**Expected result** (per official API documentation):

- Missing parameter -> 400
- Invalid credentials -> 404

**Actual result**: Both cases return status code 200, with the correct error message in the response body, but the wrong status code.

**Severity**: Low
**Priority**: Low
