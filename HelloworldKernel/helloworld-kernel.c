// Weird hello world kernel module for Linux.

#include <linux/init.h>
#include <linux/module.h>
#include <linux/uaccess.h>
#include <linux/fs.h>
#include <linux/proc_fs.h>


MODULE_AUTHOR("Joe Jagger");
MODULE_DESCRIPTION("Hello world driver");
MODULE_LICENSE("ZILCH!");



static int __init custom_init(void) {
    printk(KERN_INFO "Does the body rule the mind?");
    return 0;
}
static void __exit custom_exit(void) {
    printk(KERN_INFO "Adios.");
}
module_init(custom_init);
module_exit(custom_exit);