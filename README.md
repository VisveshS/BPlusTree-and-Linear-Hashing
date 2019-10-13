# <u>B+ tree and Linear Hashing implementation</u>

<p style='text-align: right;'><i>-Visvesh S Subramanian</i></p>
## <u>PART 1: B+ Tree</u>
<b><u>*class Node:*</u></b>

 * **constructor** -<br>
        A node consists of:<br>
        &middot; keys<br>
        &middot; pointers to children<br>
        &middot; pointer to next record *(NULL in case of non-leaf)*<br>
        &middot; flag - if it is leaf or not<br>
 * **split()** -<br>
        &middot; Incase node size becomes larger than 3, it needs to be split<br>
        &middot; splits node into two, returns key that needs to be added to parent and the sibling node

<b><u>*class BPlusTree:*</u></b>

 * **constructor** -<br>
        &middot; initiallize root to an empty leaf.<br>
 * **insert(record)** -<br>
        &middot; inserts record into B+ tree:<br>
&rarr; Descend to appropriate leaf and add record, split if node overflows.<br>&rarr; Recursively add this overflow to parent node.<br>&rarr;  Add new root if existing root overflows.<br>
 * **count(record)** -<br>
        &middot; Counts number of instances a record.<br>
 * **find(record)** -<br>
        &middot; Tells if record is present in B+tree or not.<br>
 * **range(low,high)** -<br>
        &middot; Counts number of records with keys in a range ∈ [<i>low, high</i>].<br>
 * **first_leaf(value)** -<br>
        &middot; Returns the first record *(from left)* who's key is greater than *value*<br>

## <u>PART 2: Linear Hashing</u>
<b><u>*class linearHash:*</u></b>

 * **constructor** -<br>
        &middot; Initializes 2 empty buckets(buckets are of size 2)<br>
        &middot; Number of decimal places used in hashing initially = 1<br>
 * **hashvalue()** -<br>
        Hash of number k is:<br>
        &rarr; k%2<sup>i</sup> if it is lesser than number of buckets *n*<br>
        &rarr; (k%2<sup>i</sup>)&minus;2<sup>i-1</sup> otherwise<br>
 * **insert(record)** -<br>
        &middot; If occupancy > <u>85%</u>, add new bucket:<br>
        &middot; If binary representation of new bucket is **1a<sub>2</sub>a<sub>3</sub>a<sub>4</sub>...** split the bucket with binary representation **0a<sub>2</sub>a<sub>3</sub>a<sub>4</sub>...** where a<sub>i</sub> ∈ {0,1} ∀ i<br>
        &middot; Add record to bucket corresponding to hash of the record<br>
 * **present(record)** -<br>
        &middot; Tells if the record already exists in hash table.<br>
 * **show()** -<br>
        &middot; Prints hash table.<br>
