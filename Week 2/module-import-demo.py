import math

greeting = "Hello, welcome to the module import demo!"

scales_played = 8
existing_major_keys = 12

scale_ratio = math.log2(scales_played / existing_major_keys) # Calculate the ratio of scales played to existing major keys
print(f"The ratio of scales played to existing major keys is: {scale_ratio:.2f}")

percentage_scales_played = math.ceil((scales_played / existing_major_keys) * 100) # Calculate the percentage of scales played
print(f"You have played {percentage_scales_played}% of the existing major keys.")