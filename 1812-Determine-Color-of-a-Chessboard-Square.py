class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        coordinates = [letter for letter in coordinates]    
        coordinates[0] = ord(coordinates[0].upper()) - ord('A') + 1
        coordinates[1] = int(coordinates[1])

        if sum(coordinates) % 2 == 0:
            return False
        else:
            return True
