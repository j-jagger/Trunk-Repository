obj-m += helloworld-kernel.o

BUILD_DIR := build-$(shell date +%Y%m%d-%H%M%S)

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules
	mkdir -p $(BUILD_DIR)
	mv *.mod *.cmd *.ko *.o *.mod.c *.order *.symvers $(BUILD_DIR) 2>/dev/null || true

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
	rm -rf build-*