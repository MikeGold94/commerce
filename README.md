# Specification

Complete the implementation of your auction site. You must fulfill the following requirements:

## Models
Your application should have at least three models in addition to the `User` model:
- **Auction Listings**: A model for auction listings.
- **Bids**: A model for bids placed on auction listings.
- **Comments**: A model for comments made on auction listings.

You may add additional models if needed. Decide the fields and their types for each model.

---

## Features

### 1. **Create Listing**
- Users should be able to create a new listing.
- Fields:
  - Title
  - Text-based description
  - Starting bid
  - Optional: URL for an image
  - Optional: Category (e.g., Fashion, Toys, Electronics, Home, etc.)

---

### 2. **Active Listings Page**
- The default route should display all currently active auction listings.
- Each listing should show:
  - Title
  - Description
  - Current price
  - Photo (if available)

---

### 3. **Listing Page**
- Clicking on a listing should display a page specific to that listing.
- Details to display:
  - Title, description, current price, and other relevant details.
- Features:
  - **Watchlist**:
    - Signed-in users can add/remove the item from their watchlist.
  - **Bidding**:
    - Signed-in users can place a bid.
    - The bid must:
      - Be at least as large as the starting bid.
      - Be greater than any existing bids.
    - If the bid doesn’t meet these criteria, an error should be shown.
  - **Close Auction**:
    - If the user created the listing, they can close the auction.
    - The highest bidder becomes the winner, and the listing becomes inactive.
  - **Winner Notification**:
    - If a user has won a closed auction, the page should notify them.
  - **Comments**:
    - Signed-in users can add comments.
    - The page should display all comments.

---

### 4. **Watchlist**
- Signed-in users can visit a Watchlist page.
- The page should display all listings the user has added to their watchlist.
- Clicking on a listing should take the user to that listing’s page.

---

### 5. **Categories**
- A page should display a list of all listing categories.
- Clicking on a category should show all active listings in that category.

---

### 6. **Django Admin Interface**
- The Django admin interface should allow administrators to:
  - View, add, edit, and delete listings, comments, and bids.

---

## Hints
- To create a superuser account for the Django admin interface, run:
  ```bash
  python manage.py createsuperuser