import parrot
import time

ir_code = parrot.IR_encode()

ir = parrot.IR()
ir_buff = ir_code.encode_nec(1, 85)
while True:
    ir.send(ir_buff, 1)
    time.sleep(3)
    ir.stop_send()
    time.sleep(3)