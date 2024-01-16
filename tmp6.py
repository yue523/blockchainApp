import hashlib

def merkle_root(hash_array):
    if len(hash_array) == 0:
        return None

    while len(hash_array) > 1:
        temp = []
        for i in range(0, len(hash_array)-1, 2):
            combined_hash = hash_array[i] + hash_array[i+1]
            hash_object = hashlib.sha256(combined_hash.encode())
            temp.append(hash_object.hexdigest())

        # If the number of hashes is odd, duplicate the last one
        if len(hash_array) % 2 == 1:
            temp.append(hash_array[-1])

        hash_array = temp

    return hash_array[0]

# 8つのハッシュ値の例
hash_array = [
    "hash1", "hash2", "hash3", "hash4",
    "hash5", "hash6", "hash7", "hash8"
]

merkle_root_value = merkle_root(hash_array)
print("Merkle Root:", merkle_root_value)
