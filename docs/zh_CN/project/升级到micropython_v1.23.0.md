升级mpython micropython

micropython v1.23.0

esp-idf v5.0.4

# esp32项目

    esp-idf采用cmake构建编译系统，micropython现支持make和使用idf.py编译系统。make内部也是调用idf.py实现，因些需要了解esp32的编译。
    说明：esp32把用户的应用代码称之为项目。esp-idf不是项目的一部分。
    esp32项目管理：
    参考文档：<https://docs.espressif.com/projects/esp-idf/zh_CN/latest/esp32/>

    关于esp32的构建系统，了解：

    1. 项目及主程序概念
    2. 构建系统，idf.py
    3. 组件 main组件
    4. 示例项目
    5. CMakeList.txt
    6. sdkconfig

# micropython项目架构

## micropython相关知识

### 模块编写

### 功能配置

### python引用C

### QSTR

### 模块注册 模块使能

### 把C变量纳入micropython gc内存管理

    参照modespnow做法，例如把_esp_espnow_obj_t *espnow_singleton加入gc管理：

    1. gc内存管理结构中，加入*espnow_singleton

        ```c
        MP_REGISTER_ROOT_POINTER(struct _esp_espnow_obj_t *espnow_singleton);
        ```

    2、espnow_make_new()中获取指针

        此函数中，esp_espnow_obj_t *self = MP_STATE_PORT(espnow_singleton)获取指针，如果为空，说明对应内存被释放，需新建。

    3、模块使用此变量

        get_singleton()可获取注岫在gc内存管理结构中的本变量指针，然后模块就可以使用它了。get_singleton()内部也是调用MP_STATE_PORT(espnow_singleton)

## micropython做为esp-idf项目

micropython整体做为一个基于esp-idf项目,被定义在main组件中，但项目的文件夹还是保留micropython的框架，main组件被重命名为几个main_xxx，对应不同的几款ESP芯片。main组件的源文件配置，在port/esp32_common.cmake中配置。

1. 项目顶层CMakeList.txt

    位于port下。定义下以下内容
    - IDF_VERSION
    - MICROPY_BOARD
    - MICROPY_BOARD_DIR
    - SDKCONFIG #合并后的sdkconfig文件位置
    - include(${MICROPY_BOARD_DIR}/mpconfigboard.cmake)

        mpconfigboard.cmake定义了1、各个板的MICROPY_FROZEN_MANIFEST位置（当然也可能没定义）2、SDKCONFIG_DEFAULTS，各个板的skdconfig.xxx集合，有这两项，就可以做下面两件事。

        1. 定义MICROPY_FROZEN_MANIFEST # mainfest.py位置，通常在各个板目录下，如果没有，则用boards下的。
        2. 定义SDKCONFIG_DEFAULT #

            合并各个sdkcofig.xxx 生成sdkconfig.combobin,各个板其于sdkconfig.base，定制n个sdkconfig.xxx，用于实现不同的config，后面的配置会覆盖前面的配置？micropython中通过sdkconfig.base + 多个sckconfig.xxx来实现不同的配置，最后合并成config.combobin
    - list(APPEND EXTRA_COMPONENT_DIRS main_${IDF_TARGET})

        重命名main组件，且通过这个区别项目用哪个esp芯片。各个不同芯片的main组件目录下，包含以下文件：
        - CMakeList.txt：

            该芯片main组件的CMakeList.txt文件，会包含esp32_common.cmake（公用的cmake配置），及各芯片自已的一些配置

        - idf_component.yml: Component Manager Manifest File,用于加入esp其它级件
        - link.if

2. mainfest.py

    官方参考文档：<https://docs.micropython.org/en/latest/reference/manifest.html>

    MicroPython除了能够从文件系统加载Python代码外，还可以把Python代码“冻结”到固件加载，这样做有几个好处：
代码已被预编译为字节码，无需在加载时编译Python源代码。
字节码可以直接从ROM（即闪存）中执行，而无需复制到内存。同样，任何常量对象（字符串、元组等）也从ROM中加载，这可以大大增加应用程序的可用内存。
在没有文件系统的设备上，这也是加载Python代码的唯一方法。

    项目中，如果boards/xxx板文件夹中有manifest.py，则用此文件件，此文件会包含port/boards/manifest.py，否则直接用port/boards/manifest.py。

# mpython项目组建

1. 创建mpython项目文件夹

    创建文件夹，并初始化仓库，推送到远程。

2. 创建子模块

    项目添加esp-idf及micrpython子模块，从官方拉取项目，并分别checkout到v5.0.4，v1.23.0，然后在项目文件夹下执行：

    ```bash
    git submodule updatee --init --recursive
    ```

    拉取所有子模块。

3. 新建port文件夹

    把以下文件（文件夹），从micropython/ports/esp32复制到port文件夹。

    - boards 、README.md，README.ulp.md
    - main_xxx文件兲：不同芯片的main组件。
    - 顶层CMakeLists.txt
    - esp32_common.cmake：是所有板的公共cmake文件。
    - modules：所有板的公用python库。

4. 相关修改

    修改esp31_common.cmake内MICROPY_DIR MICROPY_PORT_DIR路径定义。
    复制对应的partitions-xxx.csv到boards/对应board，修改，在sdkconfig.board中修改partitions-xxx路径为当前board。
    PSRAM支持：复制sdkconfig.spiram到当前board下，修放（配置引脚、容量），配置mpconfigboard.cmake中配置本路径。
    esp32_common.cmake中修改qstrdefsport.h路径

Noto_Sans_CJK_SC_Light16.bin .gitignore过来，把.gitignore内容复制过来。

_boot.py
TAG
板名

# 项目编译

linux系统按乐鑫要求安装一些库，安装gcc cmake

1. 进入esp-idf，执行./install.sh，安装esp-idf的编译环境。
2. 执行.

    ```bash
    cd port
    ./esp-idf/export.sh # 导出相关环境变量。
    ```

3. micropython预编译

    ```bash
    cd micropython
    make -C mpy-cross
    ```

4. 固件编译

    ```bash
    cd port
    idf.py -D MICROPY_BOARD=labplus_classroom_kit_nanjing build
    idf.py -D MICROPY_BOARD=labplus_Ledong build
    idf.py -D MICROPY_BOARD=mpython build
    ```

5. 固件烧录

    ```bash
    idf.py -p /dev/ttyACM0 -b 1500000 flash
    ```

    esptool命令：

    ```bash
        esptool.py \
            --port $port --baud $baud --before default_reset --after hard_reset write_flash \
            --flash_mode dio --flash_freq 40m --flash_size detect 0x410000 "$file"
    ```

    要在wsl下使用USB设备，参阅：<https://learn.microsoft.com/zh-cn/windows/wsl/connect-usb，安装USBIPD-WIN。>
    使用以下指令，实现USB设备共享到wsl。

    ···bash
    usbipd list # 列出usb设备ID，powershell中执行命令
    usbipd bind --busid <busid> # bind ID，eg:4-4
    usbipd attach --wsl --busid <busid> # 附加USB设备到wsl
    lsusb # wsl下，查看USB设备是否附加。
    usbipd attach --wsl --busid <busid> # 解除附加USB设备到wsl

6. 调试

    vscode安装插件pymakr

# 添加乐动掌控

    按以上步聚创建完mpython项目。

1. C层面添加OLED驱动及开机LOG显示

        涉及port/drivers/startup main.c

2. 底层python异常显示在oled

    涉及port/drivers/startup main.c,包括按CTRL C停止所有用户线程，关闭所有用户定时器。

3. 添加音乐模块

    port/qstrdefsport.h中添加music相关QSTR.
    mpconfigboard.cmake中把builtin音乐模块源文件加入项目，按新的micropython模块定义方式修改。
    mpconfigboard中使能本模块。
    music源码中，增加#if MICROPY_PY_ESP_MUSIC,用于使能/禁能模块

4. esp32_nvs

    复制micropython/ports/esp32/下对应模块到port/builtins/，make_new()中增加以下代码:

    ```c
    check_esp_err(nvs_flash_init_partition("user_nvs"));
    check_esp_err(nvs_open_from_partition("user_nvs", ns_name, NVS_READWRITE, &namespace));
    ```

    esp32_common.cmake中去掉esp32_nvs.c，mpconfigboard.cmake中增加port/builtins/eps32_nvs.c

5. machine_pin.c
   esp32_common.cmake去掉对machine_pin.c编译，复制micropython/ports/esp32/machine_pin.c到port/builtins/，此文件添加mpython pin定义。
   micropython对有PSRAM的板，限定的CS CLK pin为16 17引脚，需要重新修改machine.h为_machine.h，去掉对16 17脚的禁用。esp32_common.cmake重定义pins_prefix.c make-pins.py路径

6. 修改partition-8MiB.csv文件

    保持跟乐动掌控的一致，但会出固件区域不够情况，扩容之，暂不知会有什么问题，之前似似乎有利用扩容区。此文件放在对应board文件下，注意在sdkconfig.board中修改文件路径.

7. 添加micropython-lib库的neopixel.py到port/modules,参照唐工的对应文件做修改。注释掉boards/manifest.py内的对本库的引用。

8. machine_touchpad.c

   esp32_common.cmake去掉对machine_touchpad.c编译，复制micropython/ports/esp32/machine_touchpad.c到port/builtins/，按之版本修改本文件。
   mpconfigboard.cmake添加此文件编译

9. modframebuf.c

    esp32_common.cmake中禁止modframbuf.c编译，board/mpconfigboard.cmake添加此文件编译。按之前版本做相应修改。此文件影响mpython.py中的GUI库
    可以用以下命令移除变量或列表中的一项：

    ···bash
    list(REMOVE_ITEM MICROPY_SOURCE_EXTMOD ${MICROPY_EXTMOD_DIR}/modframebuf.c)

    ```

    待解决：一些函数重定义了，是否用新版的函数，待用户端测试

10. network and radio

11. 离线语音识别及合成

    参考文档：<https://docs.espressif.com/projects/esp-sr/zh_CN/latest/esp32/getting_started/readme.html>

    参考项目：<https://github.com/espressif/esp-skainet>

    main_esp32/idf_componnet.yml中添加esp-sr组件：espressif/esp-sr: ">=1.7.0"

4. bluetooth

5. tag
