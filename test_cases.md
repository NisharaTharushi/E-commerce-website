## Page Load

| Test Case ID | Test Description                         | Steps                                                              | Expected Result                                                      |
|--------------|------------------------------------------|--------------------------------------------------------------------|----------------------------------------------------------------------|
| PL_01        | Verify page loads successfully           | Navigate to https://www.automationexercise.com                     | Homepage loads completely without any errors                         |
| PL_02        | Verify page load time                    | Open browser dev tools > Reload page > Check loading time          | Page load time is under acceptable threshold (e.g., < 3 seconds)     |
| PL_03        | Verify no broken elements on load        | Load homepage > Inspect UI elements                                | All images, styles, scripts load correctly without console errors    |
| PL_04        | Verify page loads on different browsers  | Open site on Chrome, Firefox, Edge                                 | Page loads consistently on each browser                              |
| PL_05        | Verify page loads on mobile devices      | Open site on mobile browser or use device emulator                 | Page loads properly on mobile with responsive layout                 |
| PL_06        | Verify HTTPS security is active          | Check browser address bar                                          | Padlock icon is visible; page uses HTTPS                             |
| PL_07        | Verify favicon is displayed              | Open homepage > Check browser tab                                  | Automation Exercise favicon is visible                               |

## Page Title

| Test Case ID | Test Description                         | Steps                                                              | Expected Result                                                      |
|--------------|------------------------------------------|--------------------------------------------------------------------|----------------------------------------------------------------------|
| PT_01        | Verify homepage title                    | Load homepage > Check browser tab title                            | Title is "Automation Exercise"                                       |
| PT_02        | Verify title is consistent across sessions| Open homepage > Refresh multiple times                             | Title remains the same                                               |
| PT_03        | Verify title tag in HTML                 | Right-click > View page source > Search <title> tag                | <title>Automation Exercise</title> is present                        |
| PT_04        | Verify title on different browsers       | Open site on Chrome, Firefox, Safari                               | Title displays correctly in each browser tab                         |
| PT_05        | Verify title encoding                    | Load homepage and inspect for symbols/characters                   | Title does not show any broken characters or encoding issues         |

## Logo

| Test Case ID | Test Description                         | Steps                                                              | Expected Result                                                      |
|--------------|------------------------------------------|--------------------------------------------------------------------|----------------------------------------------------------------------|
| LOGO_01      | Verify logo is displayed                 | Open homepage                                                      | Logo is visible at the top-left corner                               |
| LOGO_02      | Verify logo size is consistent           | Inspect logo size via browser dev tools                            | Logo dimensions match design specifications                          |
| LOGO_03      | Verify logo redirects to homepage        | Click on the logo                                                  | Redirects to homepage (/index.html)                                  |
| LOGO_04      | Verify logo is aligned properly in header| Observe logo placement in header                                   | Logo is properly aligned (left/top as per design)                    |
| LOGO_05      | Verify logo is not blurry                | View logo at standard and high resolutions                         | Logo should be high quality and not pixelated                        |
| LOGO_06      | Verify logo has alt text                 | Inspect HTML of logo element                                       | Logo image has alt="Website for automation practice"                 |

## Header Navigation

| Test Case ID | Test Description                         | Steps                                                              | Expected Result                                                      |
|--------------|------------------------------------------|--------------------------------------------------------------------|----------------------------------------------------------------------|
| Header_01    | Verify logo is visible                   | Navigate to homepage                                               | Logo is displayed at the top-left corner                             |
| Header_02    | Verify logo redirects to homepage        | Click on the logo                                                  | User is redirected to homepage                                       |
| Header_03    | Verify 'Home' link is visible            | Navigate to homepage                                               | 'Home' link is present in header                                     |
| Header_04    | Verify 'Home' link is clickable          | Click 'Home' link                                                  | Page reloads or stays on homepage                                    |
| Header_05    | Verify 'Products' link redirects         | Click on 'Products'                                                | User is redirected to /products                                      |
| Header_06    | Verify 'Cart' link redirects             | Click on 'Cart' link                                               | User is redirected to /view_cart                                     |
| Header_07    | Verify 'Signup / Login' redirects        | Click on 'Signup / Login'                                          | User is redirected to /login                                         |
| Header_08    | Verify 'Contact Us' link redirects       | Click on 'Contact Us'                                              | User is redirected to /contact_us                                    |
| Header_09    | Verify 'Test Cases' link redirects       | Click on 'Test Cases'                                              | User is redirected to /test_cases                                    |
| Header_10    | Verify 'API Testing' link redirects      | Click on 'API Testing'                                             | User is redirected to /api_list                                      |
| Header_11    | Verify 'Video Tutorials' link            | Click on 'Video Tutorials'                                         | User is redirected to YouTube tutorial playlist                      |
| Header_12    | Verify 'Logout' appears after login      | Log in > Check header                                              | 'Logout' option should be visible                                    |
| Header_13    | Verify 'Signup / Login' hidden after login| Log in > Check header                                             | 'Signup / Login' link is hidden                                      |
| Header_14    | Verify username appears in header        | Log in > Observe header                                            | Welcome message with username should appear                          |
| Header_15    | Verify 'Logout' logs out user            | Log in > Click 'Logout'                                            | User is logged out and redirected to home                            |
| Header_16    | Verify header navigation alignment       | View header on desktop                                             | All nav items are horizontally aligned                               |
| Header_17    | Verify search box is present             | Check header                                                       | Search input field is visible                                        |
| Header_18    | Verify placeholder text in search box    | Check search input                                                 | Placeholder shows 'Search Product'                                   |
| Header_19    | Verify text input in search bar          | Type 'dress' into search box                                       | Text is entered correctly                                            |
| Header_20    | Verify search icon is visible            | Check header                                                       | Search icon/button appears next to input field                       |
| Header_21    | Verify search functionality              | Type keyword > Click search icon                                   | Redirects to products page with results                              |
| Header_22    | Verify cart icon updates on add          | Add item to cart                                                   | Cart icon updates to show item count                                 |
| Header_23    | Verify responsive header on small screen | Resize browser or open on mobile                                   | Header collapses into hamburger menu                                 |
| Header_24    | Verify hamburger opens menu links        | On mobile, click hamburger icon                                    | All nav links become visible                                         |
| Header_25    | Verify 'Recommended Items' link          | Click 'Recommended Items'                                          | Scrolls to or highlights the recommended section                     |
| Header_26    | Verify no JS errors on link click        | Open dev tools > Click header links                                | No JavaScript errors in console                                      |

## Products Page

| Test Case ID | Test Description                         | Steps                                                              | Expected Result                                                      |
|--------------|------------------------------------------|--------------------------------------------------------------------|----------------------------------------------------------------------|
| PROD_P_01    | Verify that the Products page loads       | Navigate to https://www.automationexercise.com/products            | Products page loads without errors                                   |
| PROD_P_02    | Verify page title is “All Products”       | Open the Products page                                             | Page title is displayed as "All Products"                            |
| PROD_P_03    | Verify all products are listed            | Open the Products page                                             | All available products are listed                                    |
| PROD_P_04    | Verify product images are visible         | Open the Products page                                             | Each product shows a visible image                                   |
| PROD_P_05    | Verify product names are displayed        | Open the Products page                                             | Each product’s name is visible                                       |
| PROD_P_06 | Verify product prices are displayed | Open the Products page | Each product’s price is visible |
| PROD_P_07 | Verify product descriptions/brief info are shown | Open the Products page | Product descriptions or brief info are visible |
| PROD_P_08 | Verify the presence of the search bar on the Products page | Open the Products page | Search bar is visible |
| PROD_P_09 | Verify the presence of category filters (e.g., Women, Men, Kids) | Open the Products page | Category filters (Women, Men, Kids) are displayed |
| PROD_P_10 | Verify the presence of brand filters (e.g., H&M, Polo, Biba) | Open the Products page | Brand filters (H&M, Polo, Biba, etc.) are displayed |
| PROD_P_11 | Verify presence of "Add to Cart" buttons | Open the Products page | "Add to Cart" buttons are visible for each product |
| PROD_P_12 | Verify footer/header displayed | Open the Products page | Footer and header are displayed correctly |
| PROD_P_13 | Verify that entering a valid product name in the search bar displays matching products | Enter valid product name in search bar > Submit search | Matching products are displayed |
| PROD_P_14 | Verify invalid product search shows no results message | Enter invalid product name > Submit search | “No products found” message is displayed |
| PROD_P_15 | Verify partial search terms return relevant results | Enter partial product name > Submit search | Relevant products matching partial term are displayed |
| PROD_P_16 | Verify search is case-insensitive | Search using upper/lowercase letters | Results are same regardless of case |
| PROD_P_17 | Verify search field can be cleared/reset | Enter text > Clear/reset field | Field is cleared and ready for new input |
| PROD_P_18 | Verify search results load timely | Perform product search | Results load without delay |
| PROD_P_19 | Verify category filter (e.g., Women) works | Select “Women” filter | Products belong only to Women category |
| PROD_P_20 | Verify brand filter (e.g., H&M) works | Select H&M brand filter | Only H&M products are shown |
| PROD_P_21 | Verify filters can be cleared/reset | Apply filters > Clear | Filters cleared, all products shown |
| PROD_P_22 | Verify combined filters (category + brand) work | Apply both filters | Products matching both filters displayed |
| PROD_P_23 | Verify UI updates dynamically after applying filters | Apply/remove filters | Product list updates without reload |
| PROD_P_24 | Verify no products message when filters yield no results | Apply filters with no results | “No products found” message is shown |
| PROD_P_25 | Verify clicking “Add to Cart” adds product to cart | Click “Add to Cart” button | Product is added to the cart |
| PROD_P_26 | Verify cart icon/counter updates after adding product | Add product to cart | Cart counter shows correct count |
| PROD_P_27 | Verify multiple different products can be added to cart | Add different products | All products appear in cart |
| PROD_P_28 | Verify quantity can be adjusted in cart | Add product > Change quantity | Quantity and price update |
| PROD_P_29 | Verify adding same product increases quantity | Add same product multiple times | Quantity increases in cart |
| PROD_P_30 | Verify clicking cart icon navigates to cart page | Click cart icon | Cart page opens with products |
| PROD_P_31 | Verify cart page displays correct product details | Open cart page | Correct name, quantity, price shown |
| PROD_P_32 | Verify removing product from cart | Remove product from cart page | Product is removed, cart updates |
| PROD_P_33 | Verify total price calculation in cart | Add multiple products | Total = sum of price × quantity |
| PROD_P_34 | Verify “Proceed to Checkout” is present & functional | Locate and click it | User navigated to checkout page |
| PROD_P_35 | Verify clicking product image/name opens product details | Click image/name | Product detail page opens |
| PROD_P_36 | Verify product details page displays full info | Open product detail page | Image, description, specs shown |
| PROD_P_37 | Verify “Add to Cart” works on product details page | Click “Add to Cart” | Product added to cart |
| PROD_P_38 | Verify back button returns user to product listing | Use back or click “All Products” | Returns to product list |
| PROD_P_39 | Verify responsiveness on desktop | Open on desktop | Page displays correctly |
| PROD_P_40 | Verify responsiveness on tablet | Open on tablet | Page adjusts properly |
| PROD_P_41 | Verify responsiveness on mobile | Open on mobile | UI adjusts, elements accessible |
| PROD_P_42 | Verify Add to Cart is clickable on mobile | Open on mobile | Buttons are visible and clickable |
| PROD_P_43 | Verify page load time is acceptable | Load products page | Page loads < 3 seconds |
| PROD_P_44 | Verify search/filter results load quickly | Perform action | Results display promptly |
| PROD_P_45 | Verify adding to cart doesn’t freeze page | Add products | Page remains functional |
| PROD_P_46 | Verify search rejects script/SQL injection | Enter script/SQL | Input is sanitized, no error |
| PROD_P_47 | Verify search accepts only valid characters | Enter invalid chars | Input handled gracefully |
| PROD_P_48 | Verify unauthenticated user can’t access cart/checkout | Try accessing cart/checkout | Redirected to login |
| PROD_P_49 | Verify presence of email subscription input | Open products page | Subscription field visible |
| PROD_P_50 | Verify valid email subscription | Enter valid email > Submit | Confirmation shown |
| PROD_P_51 | Verify invalid email subscription | Enter invalid email > Submit | Error message displayed |
| PROD_P_52 | Verify subscription confirmation message | Subscribe with valid email | Success message displayed |
| PROD_P_53 | Verify all links on product page navigate correctly | Click header/footer/product links | Correct pages open |
| PROD_P_54 | Verify logo navigates to homepage | Click logo | Homepage loads |
| PROD_P_55 | Verify browser back/forward buttons work properly | Use browser navigation | Pages load as expected |
# Login Page – Manual Test Case Documentation

| Test Case ID | Test Description                               | Steps                                                        | Expected Result                                              |
|--------------|------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|
| LOGIN_P_01   | Verify login page loads successfully            | Navigate to https://www.automationexercise.com/login         | Login page loads without errors                               |
| LOGIN_P_02   | Verify page title                               | Open the login page                                           | Page title is "Login" or relevant title                       |
| LOGIN_P_03   | Verify presence of email input field            | Open the login page                                           | Email input field is visible and enabled                      |
| LOGIN_P_04   | Verify presence of password input field         | Open the login page                                           | Password input field is visible and enabled                   |
| LOGIN_P_05   | Verify presence of login button                  | Open the login page                                           | Login button is visible and enabled                           |
| LOGIN_P_06   | Verify "New User Signup!" link present           | Open login page                                              | Link/button to sign up new user is visible                    |
| LOGIN_P_07   | Verify password field masks input                 | Type in password field                                       | Password characters are masked (not visible as plain text)   |
| LOGIN_P_08   | Verify login with valid credentials               | Enter valid email and password, click login                  | User is logged in and redirected to user dashboard/home page |
| LOGIN_P_09   | Verify login with invalid email                    | Enter invalid email format, any password, click login        | Appropriate error message appears (e.g., "Invalid email")    |
| LOGIN_P_10   | Verify login with incorrect password               | Enter valid email, incorrect password, click login           | Error message shown (e.g., "Incorrect password")             |
| LOGIN_P_11   | Verify login with empty email field                 | Leave email empty, enter password, click login               | Error message for empty email field                           |
| LOGIN_P_12   | Verify login with empty password field              | Enter email, leave password empty, click login               | Error message for empty password field                        |
| LOGIN_P_13   | Verify login with both fields empty                  | Leave email and password empty, click login                   | Error messages for required fields                            |
| LOGIN_P_14   | Verify email field accepts valid email format        | Enter valid email format                                      | Email input accepted                                          |
| LOGIN_P_15   | Verify email field rejects invalid format            | Enter invalid email format (e.g., missing '@')               | Validation error or prevents submission                       |
| LOGIN_P_16   | Verify password field accepts characters              | Enter any characters (alphabets, numbers, special chars)     | Password input accepts characters                             |
| LOGIN_P_17   | Verify "Forgot Password?" link presence                | Open login page                                              | "Forgot Password?" link is visible                            |
| LOGIN_P_18   | Verify "Forgot Password?" link navigates correctly      | Click "Forgot Password?" link                                | Navigates to password recovery page                           |
| LOGIN_P_19   | Verify login button disabled/enabled logic             | Initially check login button status                           | Login button enabled only when required fields filled        |
| LOGIN_P_20   | Verify login with SQL injection attempt                  | Enter SQL injection string in email/password fields          | Input sanitized and error shown; no login success            |
| LOGIN_P_21   | Verify login with script injection attempt               | Enter JavaScript code in email/password fields                | Input sanitized; no script execution or errors               |
| LOGIN_P_22   | Verify session is created after login                    | Login with valid credentials                                  | User session is created                                      |
| LOGIN_P_23   | Verify user cannot access protected pages without login | Try to access protected pages without login                   | Redirected to login page                                     |
| LOGIN_P_24   | Verify user can logout after login                         | Login, click logout                                          | User is logged out and redirected to home/login page         |
| LOGIN_P_25   | Verify error message disappears after correction          | Enter invalid data, get error message, correct input          | Error message disappears once valid input is entered         |
| LOGIN_P_26   | Verify password input max length                           | Enter password exceeding max length (e.g., 50 chars)          | Input limited or truncated accordingly                        |
| LOGIN_P_27   | Verify email input max length                              | Enter email exceeding max length                             | Input limited or truncated accordingly                        |
| LOGIN_P_28   | Verify tab order of fields/buttons                          | Press Tab key repeatedly on login page                        | Focus moves logically (email → password → login)             |
| LOGIN_P_29   | Verify login page is responsive                             | Open login page on mobile/tablet/desktop                      | Elements adjust properly to screen size                       |
| LOGIN_P_30   | Verify login page paste behavior on password field          | Try to paste password in password field                       | Paste functionality disabled or allowed as per design        |
| LOGIN_P_31   | Verify user redirected to homepage after successful login   | Login with valid credentials                                  | User redirected to homepage or dashboard                      |
| LOGIN_P_32   | Verify error messages are user-friendly                      | Trigger invalid login attempts                                | Messages are clear and informative                            |
| LOGIN_P_33   | Verify login button visually indicates click                 | Click login button                                           | Button changes appearance or gives feedback                   |
| LOGIN_P_34   | Verify social login buttons present (if any)                 | Check for social login options                               | Social login buttons (Google, Facebook, etc.) visible        |
| LOGIN_P_35   | Verify error message for locked/disabled accounts            | Attempt login with locked account                            | Appropriate error message displayed                           |

---

# Cart Page – Manual Test Case Documentation

| Test Case ID | Test Description                          | Steps                                                      | Expected Result                                            |
|--------------|-----------------------------------------|------------------------------------------------------------|------------------------------------------------------------|
| CART_P_01   | Verify View Cart page loads correctly      | Navigate to https://www.automationexercise.com/view_cart   | Page loads with proper title and cart content section       |
| CART_P_02   | Verify cart is empty on first visit         | Navigate to cart page without adding any items             | Message like "Cart is empty" displayed                      |
| CART_P_03   | Verify added product is displayed in cart  | Add product to cart, navigate to View Cart page            | Product name, quantity, price, and total displayed          |
| CART_P_04   | Verify quantity of product displayed correctly | Add same product multiple times, go to View Cart            | Quantity column shows total number of items                  |
| CART_P_05   | Verify Remove (X) icon removes product       | Add product to cart, click X icon beside it                 | Product removed from cart                                    |
| CART_P_06   | Verify total price is calculated correctly   | Add multiple items with known prices                        | Total equals sum of (quantity × price) for all products     |
| CART_P_07   | Verify "Proceed To Checkout" button exists    | Visit cart page                                             | "Proceed To Checkout" button visible and clickable          |
| CART_P_08   | Verify "Continue Shopping" button works       | Click "Continue Shopping"                                   | Redirects to products page                                   |
| CART_P_09   | Verify cart persists after page refresh        | Add product, refresh View Cart page                         | Product still appears in cart                                |
| CART_P_10  | Verify cart persists across sessions (if logged in) | Login, add item, logout, login again                        | Items remain in cart                                         |
| CART_P_11  | Verify cart clears on user logout                | Add item while logged in, logout                            | Cart resets or empties                                       |
| CART_P_12  | Verify user can update product quantity manually | Go to cart page, edit quantity field manually              | Quantity updates, total price adjusts                        |
| CART_P_13  | Verify UI elements alignment                      | View cart page                                              | Product rows, buttons, pricing properly aligned             |
| CART_P_14  | Verify product image is visible in cart           | Add product, go to cart                                     | Product image shown beside product name                      |
| CART_P_15  | Verify product price visibility                     | Add product to cart                                         | Product price shown correctly                                |
| CART_P_16    | Verify alert shown when clicking "Proceed to Checkout" logged out | 1. Visit View Cart page without logging in 2. Click "Proceed To Checkout" | Alert pops up with Register/Login options and "Continue with Cart" button                           |
| CART_P_17    | Verify "Register / Login" link redirects to login page      | 1. In alert popup, click "Register / Login" link                       | User is taken to the login/signup page                                                            |
| CART_P_18    | Verify "Continue with Cart" redirects to checkout           | 1. In alert popup, click "Continue with Cart"                          | User is redirected to checkout page                                                               |
| CART_P_19    | Verify alert message text content                            | 1. Click "Proceed To Checkout" as guest                                | Alert message includes prompt to log in or continue as guest                                      |
| CART_P_20    | Verify alert closes after choosing an option                | 1. Click "Register / Login" or "Continue with Cart"                    | Alert disappears                                                                                   |
| CART_P_21    | Verify alert does not appear if already logged in            | 1. Log in 2. Add product to cart 3. Go to cart page 4. Click "Proceed To Checkout" | No alert appears; user is redirected directly to checkout                                         |
| CART_P_22    | Verify back button from alert page functions correctly       | 1. Click "Proceed To Checkout" → alert appears → press browser back    | Should go back to cart page                                                                        |

---

# Contact Us Page – Manual Test Case Documentation

| Test Case ID | Test Description                                           | Steps                                                        | Expected Result                                                                          |
|--------------|------------------------------------------------------------|--------------------------------------------------------------|------------------------------------------------------------------------------------------|
| CONTA_P_01   | Verify Contact Us page loads correctly                     | Navigate to https://www.automationexercise.com/contact_us    | Contact Us page loads successfully with all elements visible                             |
| CONTA_P_02   | Verify page title                                          | Open Contact Us page                                         | Page title contains "Contact Us" or relevant title                                      |
| CONTA_P_03   | Verify presence of Name input field                         | Open Contact Us page                                         | Name input field is visible and enabled                                                 |
| CONTA_P_04   | Verify presence of Email input field                        | Open Contact Us page                                         | Email input field is visible and enabled                                                |
| CONTA_P_05   | Verify presence of Subject input field                      | Open Contact Us page                                         | Subject input field is visible and enabled                                              |
| CONTA_P_06   | Verify presence of Message textarea                         | Open Contact Us page                                         | Message textarea is visible and enabled                                                 |
| CONTA_P_07   | Verify presence of Submit button                            | Open Contact Us page                                         | Submit button is visible and enabled                                                   |
| CONTA_P_08   | Verify Name field accepts input                             | Enter valid name in Name field                               | Input is accepted                                                                       |
| CONTA_P_09   | Verify Email field accepts valid email                      | Enter valid email format in Email field                      | Input accepted                                                                         |
| CONTA_P_10   | Verify Email field rejects invalid email                    | Enter invalid email format in Email field (e.g., missing '@') | Error message displayed or validation fails                                           |
| CONTA_P_11   | Verify Subject field accepts input                          | Enter text in Subject field                                  | Input accepted                                                                         |
| CONTA_P_12   | Verify Message field accepts input                          | Enter text in Message textarea                               | Input accepted                                                                         |
| CONTA_P_13   | Verify submitting form with all valid fields                | Fill all fields with valid data, click Submit                | Success message displayed (e.g., "Success! Your details have been submitted successfully.") |
| CONTA_P_14   | Verify error message on empty Name                          | Leave Name empty, fill other fields, click Submit            | Error message indicating Name is required                                             |
| CONTA_P_15   | Verify error message on empty Email                         | Leave Email empty, fill other fields, click Submit           | Error message indicating Email is required                                            |
| CONTA_P_16   | Verify error message on invalid Email format                | Enter invalid email format, fill other fields, click Submit | Error message about invalid email                                                     |
| CONTA_P_17   | Verify error message on empty Subject                       | Leave Subject empty, fill other fields, click Submit         | Error message indicating Subject is required                                          |
| CONTA_P_18   | Verify error message on empty Message                       | Leave Message empty, fill other fields, click Submit         | Error message indicating Message is required                                          |
| CONTA_P_19   | Verify form does not submit if any required field is empty | Leave any required field empty, click Submit                  | Form is not submitted; validation errors shown                                        |
| CONTA_P_20   | Verify message displays after successful submission         | Submit form with valid data                                   | Confirmation/success message appears                                                  |
| CONTA_P_21   | Verify form resets after successful submission              | Submit form with valid data, check if form fields clear      | Form fields are cleared                                                               |
| CONTA_P_22   | Verify input max length for Name field                      | Enter very long input (e.g., 255+ chars) in Name field       | Input truncated or error shown                                                        |
| CONTA_P_23   | Verify input max length for Subject field                   | Enter very long input in Subject field                        | Input truncated or error shown                                                        |
| CONTA_P_24   | Verify input max length for Message field                   | Enter very long text in Message textarea                      | Input truncated or error shown                                                        |
| CONTA_P_25   | Verify email field does not accept scripts (XSS prevention) | Enter script tags or JavaScript code in Email field          | Input sanitized, no script execution                                                  |
| CONTA_P_26   | Verify form submission with SQL Injection string in inputs  | Enter SQL injection strings in any input field                | Input sanitized, no SQL injection possible                                            |
| CONTA_P_27   | Verify Submit button disabled/enabled logic                 | Observe Submit button when fields are empty and when filled  | Button disabled when required fields empty; enabled otherwise                         |
| CONTA_P_28   | Verify CAPTCHA presence (if any)                            | Check for CAPTCHA presence on the page                        | CAPTCHA is visible                                                                    |
| CONTA_P_29   | Verify form can be submitted multiple times                 | Submit form repeatedly with valid data                        | Form submits successfully each time                                                  |
| CONTA_P_30   | Verify responsiveness of Contact Us page                    | Open page on different device sizes                           | Page layout adapts correctly                                                         |
| CONTA_P_31   | Verify all input fields have proper labels                   | Inspect form fields                                           | Each input has an associated label                                                   |
| CONTA_P_32   | Verify tab order for all fields and buttons                  | Use tab key to navigate form                                  | Focus moves logically through Name → Email → Subject → Message → Submit              |
| CONTA_P_33   | Verify presence of company contact info                      | Scroll through Contact Us page                                | Company address, phone, email info is visible                                        |
| CONTA_P_34   | Verify error message disappears after correction             | Enter invalid data to generate error, then correct data      | Error message disappears after valid input                                          |
| CONTA_P_35   | Verify that user cannot submit form if JavaScript disabled   | Disable JS and try to submit form                             | Form should ideally prevent submission or fallback occurs                            |
