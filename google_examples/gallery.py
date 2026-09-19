"""
You're designing a simple image album viewer.

class Image {};

class Gallery {
    vector<Image> allImages;
    vector<Image> markedFavorites;
    Gallery() {
        // some setup
    }

    Image getNext(); // Returns next image
};

You are to implement the getNext() function such that:
The images from markedFavorites should be returned first.
Then, return the remaining images from allImages that are not in markedFavorites.
Each call to getNext() should return the next image in this combined sequence.
—----------------------------------------------------------------------------------------------------------------------------
Additional information collected through clarifying questions:
Once the end is reached, getNext() should return null.
getNext() takes no parameters.
You can do some setup in the constructor, but avoid anything too costly.
Assume that markedFavorites[] is a subset of allImages[], and both vectors remain unchanged after construction.
Order among markedFavorites[] and allImages[] should be maintained.
Example Input:
allImages = {i1, i2, i3, i4, i5, i6, i7, i8, i9, i10};
markedFavorites = {i2, i5, i7};
Expected Sequence of getNext() calls:
i2, i5, i7, i1, i3, i4, i6, i8, i9, i10
"""

import uuid


class Image:
    def __init__(self, *args, **kwargs) -> None:
        # UUIDv7 provides better index locality.
        self.id: uuid.UUID = uuid.uuid7()  # Python 3.14+


class Gallery:
    def __init__(self) -> None:
        self.all_images: list[Image] = []
        self.marked_favorites: list[Image] = []

        # Stores favorite IDs for O(1) average membership checks.
        self.used_favorites: set[uuid.UUID] = set()  # Extra memory: O(f)

        self.general_idx: int = 0
        self.favorite_idx: int = 0

    def get_next(self) -> Image | None:
        """Return the next image, prioritizing favorites."""

        # Stage 1: Return all favorites first.
        if self.favorite_idx < len(self.marked_favorites):
            img: Image = self.marked_favorites[self.favorite_idx]
            self.favorite_idx += 1

            self.used_favorites.add(img.id)

            return img

        # Stage 2: Return remaining non-favorite images.
        while self.general_idx < len(self.all_images):
            img: Image = self.all_images[self.general_idx]
            self.general_idx += 1

            if img.id not in self.used_favorites:
                return img

        return None


# Time: O(n + f) total
# Extra memory: O(f)
