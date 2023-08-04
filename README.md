# group-106  
小组中的成员为：  
崔若锦 202100460014 负责project：4 5 8 17 19  
梁芮豪 202100460 负责project：  
潘浩洋 202100460136 负责project：1 2 3 9  

## project1  
这部分该部分由小组中的潘浩洋同学完成，

## project2  
## project3  
## project4  
该部分由小组成员崔若锦完成  
实验设备：  
12th Gen Intel(R) Core(TM) i7-12700H   2.30 GHz  
实验环境：  
C++：Visual Studio 2022  
python：PyCharm 2022.2.3  
（后续实验环境不变，不再赘述）  
国密算法SM3的执行过程可以概括为四个步骤：消息填充、消息扩展、迭代压缩、输出结果。下面将详细说明每个步骤：

### 1. 消息填充：
SM3算法采用Merkle-Damgard结构，在处理消息时，首先将消息进行填充，使其长度能够被512位整除。填充规则为在消息末尾添加一个"1"比特，然后添加若干个"0"比特，直到满足消息长度对512取模等于448。剩余的64位用来表示原始消息的长度，以比特为单位。

### 2. 消息扩展：
在填充后的消息基础上，进行消息扩展。将512位的消息分成16个64位的消息分组，然后通过扩展算法产生48个64位的字，用于后续的迭代压缩过程。

### 3. 迭代压缩：
迭代压缩是SM3算法的核心步骤，它通过64轮的迭代运算来混淆和压缩消息。在每一轮迭代中，使用消息扩展得到的字与初始的256位哈希值之间进行一系列的位运算和置换操作，从而逐渐更新哈希值。

### 4. 输出结果：
经过64轮迭代压缩后，最终得到256位的哈希值，即SM3算法的输出结果。该哈希值可以用作数字签名和验证，具有较高的安全性，满足密码应用中的要求。

总结来说，SM3算法是一种用于密码杂凑的算法，通过消息填充、消息扩展、迭代压缩等步骤将输入消息转换为256位的哈希值。它具有多项式时间可计算、单向性、认证性和抗碰撞性等特性，适用于数字签名和验证等商用密码应用。
### 优化方向：  
优化前：  
计算前16个wi时，每个需要执行一次load和一个store，计算后52个wi时，每个需要执行5次load，1次store，6次XOR和1次rot；  
计算64个wi，每个wi需要执行2次load，1次store和1次rot。  
优化后：  
在计算前 12 个 wi+4 时，每个都需要执行一次加载和一次保存。 在计算最后52个wi+4时，每个需要进行5次load，1次store，6次XOR，4次rot；  
主要是减少计算和存储W'时的存取操作。 在测试中，优化也提高了算法的执行速度
### 运行结果：
未加密的明文:cuirujin加密中...  
SM3加密后的密文:6e0f9e14344c5406aOcf5a3b4dfb665f87f4a771a31f7edbb5c72874a32b29571加密时间为:9.38 ms  
解密中...  
解密时间为:17.22 ms  
（没插图片就图文识别了一下）  

## project5   
### Merkle Tree
梅克尔树（Merkle Tree）是一种数据结构，它用于验证大量数据的完整性和一致性。它是由计算机科学家Ralph Merkle在1979年提出的，常用于区块链和分布式系统中，特别是在比特币和以太坊等加密货币中。

梅克尔树的核心思想是将大量数据递归地划分成小块，并使用哈希函数来生成这些数据块的哈希值。然后，将这些哈希值再递归地组合成更高层级的哈希值，直到最终形成一个根哈希值。这个根哈希值可以代表整个数据集的完整性。

下面是梅克尔树的构建过程示例，假设有四个数据块 A、B、C、D：

计算每个数据块的哈希值，得到哈希值 ha、hb、hc、hd。
组合哈希值，得到两个新的哈希值：hab = hash(ha + hb) 和 hcd = hash(hc + hd)。
再次组合哈希值，得到根哈希值 root = hash(hab + hcd)。
梅克尔树的主要好处在于：

高效验证：通过比较存储的根哈希值和其他数据块哈希值，可以快速验证数据的完整性，而无需访问或检查所有数据。
安全性：如果数据块中的任何一个数据发生改变，哈希值也会发生变化，从而使根哈希值变得不同，从而指示数据被篡改。
节省存储空间：由于梅克尔树是树状结构，它可以将大量数据用较小的根哈希值代表，节省了存储空间。
在区块链中，梅克尔树被广泛用于验证区块的交易数据是否被篡改。如果根哈希值与区块头中的哈希值匹配，就意味着整个区块的数据是完整和正确的，否则，需要对区块进行重新验证或者从其他节点请求正确的数据。这种特性使得梅克尔树成为区块链中重要的数据结构之一。

### 运行结果：  

给定message="Hello!This is Yanji123.I'm writing a merkle tree!"，可以得到一个正确的Merkle Tree.
## project8  
### AES
AES（Advanced Encryption Standard）高级加密标准是一种对称密钥加密算法，它是目前广泛使用的加密算法之一。AES于2001年由比利时密码学家Joan Daemen和Vincent Rijmen设计，并由美国国家标准与技术研究院（NIST）于2001年发布为FIPS（Federal Information Processing Standards）标准。  
AES的设计目标是提供高度安全、高效率的数据加密服务，适用于各种应用场景，包括电子邮件、虚拟私人网络（VPN）、加密通信以及保护敏感数据等。  
AES算法使用固定长度的密钥（128位、192位或256位）来加密和解密数据块，其中128位密钥版本最常用。它将数据块分为16个字节的块，每个块由4x4的矩阵组成。AES的加密和解密过程都涉及多轮迭代运算，其中每一轮都包括四个主要操作：字节替代、行位移、列混淆和轮密钥加。  
AES的四个主要操作简要解释如下：  
字节替代（SubBytes）：将每个字节替换为一个预定义的固定值，通过S盒（Substitution Box）实现，提高了算法的非线性性。  
行位移（ShiftRows）：对数据块的行进行循环位移操作，使得每一列进行位移，增加了算法的扩散性。  
列混淆（MixColumns）：通过数学运算混淆列数据，使得每一列的数据都有一定的关联性，增强算法的抵抗力。  
轮密钥加（AddRoundKey）：将密钥与数据块进行异或运算，确保每一轮的密钥都被混合到数据中。  
AES的安全性被广泛认可，它已经成为许多国家和组织的标准加密算法。相比之前的DES（Data Encryption Standard）算法，AES提供更高的安全级别和更好的性能，因此在现代加密领域得到了广泛应用。  
### ARM
ARM的架构是一种精简指令集计算机（RISC）架构，它旨在提供高性能、低功耗和高效率的处理器设计。与复杂指令集计算机（CISC）架构相比，RISC架构采用了简化的指令集，使得处理器能够更快地执行指令，并且消耗更少的能量。ARM处理器还可以高度定制，以满足不同设备和应用的需求。由于ARM架构的高效性和低功耗特点，它被广泛应用于各种领域。  
### 部分指令详解
#### vld1q_u8
vld1q_u8是ARM NEON指令集中的一条指令，用于从内存中加载一组8位无符号整数（uint8_t）数据，并将它们存储在一个128位的寄存器中。在ARM NEON中，q后缀表示这是一个128位的寄存器操作。  
具体格式为：vld1q_u8(ptr)，其中ptr是指向内存中数据的指针，通常是一个uint8_t*类型的指针。  
这条指令会从ptr指向的内存地址开始，连续读取16个8位无符号整数，并将它们存储在一个128位的寄存器中。每个8位数据占据寄存器中的一个字节。 
#### vaesmcq_u8
在ARM NEON指令集中，vaesmcq_u8是用于AES（Advanced Encryption Standard）加密算法的一条指令。它用于执行AES加密过程中的MixColumns操作中的变换。  
vaesmcq_u8指令格式为：vaesmcq_u8(uint8x16_t data)，其中uint8x16_t是一个128位的寄存器类型，表示包含16个8位无符号整数的数据。  
MixColumns是AES加密中的一个重要步骤，它对每一列进行线性变换，增加了算法的扩散性和抗攻击性。MixColumns变换将每一列看作一个多项式，然后通过多项式乘法和模运算进行变换。vaesmcq_u8指令就是用于加速这个MixColumns操作的。
#### veorq_u8
在ARM NEON指令集中，veorq_u8是用于执行按位异或（XOR）操作的一条指令。它对两个128位的寄存器中的数据进行按位异或操作，并将结果存储在一个新的128位寄存器中。  
指令格式为：veorq_u8(uint8x16_t dst, uint8x16_t src1, uint8x16_t src2)，其中uint8x16_t是一个128位的寄存器类型，表示包含16个8位无符号整数的数据。  
例如，假设有两个128位寄存器 a 和 b，它们分别包含如下数据：  
a = {0x11, 0x22, 0x33, ..., 0xEE, 0xFF}  
b = {0xAA, 0xBB, 0xCC, ..., 0x99, 0x88}  
使用veorq_u8指令执行按位异或操作后，将得到新的128位寄存器 c，其结果为：  
c = a XOR b = {0xBB, 0x99, 0xFF, ..., 0x77, 0x77}  
该指令在许多计算密集型应用中很有用，例如图像处理、加密算法等，因为它可以高效地执行并行按位异或操作，从而加快数据处理速度。  
### 运行结果：
运行过程中了解到，在VS中虽然有相对应的ARM的头文件，但是并不能正常运行，与同学沟通后，使用ARM64 msvc编译器尝试编译，在设置好配置管理器后，运行结果如下，成功编译。

## project9  
## project17  

## project19  

## project5  
