
from parrot import IR, IR_encode
import time

ir_code = IR_encode()
ir = IR()

# NEC编码
ir_buf = ir_code.encode_nec(0x01, 0x55)


while True:
    ir.send(ir_buf)
    time.sleep(1)
