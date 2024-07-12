# Reference: videohash https://github.com/akamhy/videohash/tree/main
### FFmpeg is required for python file to run properly
### FFmpeg: https://github.com/akamhy/videohash/wiki/Install-FFmpeg,-but-how%3F

from videohash import VideoHash

print("Welcome to the Video Similarity Program.\n")

# Define the URLs to the video files
url1 = input("Please enter the URL of video 1: ")
url2 = input("Please enter the URL of video 2: ")
print("\nPlease wait while we calculate the score.\n")

# Compute the video hashes
videohash1 = VideoHash(url=url1)
videohash2 = VideoHash(url=url2)

# Calculate the difference between the video hashes
hash_difference = videohash2 - videohash1

# Assuming the maximum possible difference is 100 (you can adjust this based on the expected range)
max_difference = 100.0

# Calculate the similarity score out of 100
similarity_score = max(0, (max_difference - hash_difference) / max_difference * 100)

# Compare the video hashes
print("Difference between videohash2 and videohash1:", hash_difference)  # Should be 0 if videos are identical
print("Are videohash2 and videohash1 similar?", videohash2.is_similar(videohash1))  # Should be True if videos are similar

# Print the similarity score
print(f"\nThe similarity score between the two videos is: {similarity_score:.2f}%")

