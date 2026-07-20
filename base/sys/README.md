### Модуль `sys` (System)
`sys` - предоставляет прямой доступ к переменным и функциям, которые взаимодействуют с интерпретатором Python и ОС, обеспечивая основу для создания надёжных инструментов автоматизации.

- `sys.argv` - аргументы командной строки
- `sys.exit(code)` - корректное завершение программы с указанием кода возврата
- `sys.version` - версия интерпретатора
- `sys.platform` - идентификатор платформы
- `sys.stdout` - куда пишутся логи

### Варианты запуска скриптов 
```shell
python3 argv_demo.py DevOps 
```
### или 
```shell
chmod +x argv_demo.py
```

```shell
./argv_demo.py DevOps 
```


### Полный список атрибутов модуля `sys`
- `sys.abiflags`                              `sys.implementation`
- `sys.activate_stack_trampoline(`             `sys.int_info`
- `sys.addaudithook(`                         `sys.intern(`
- `sys.api_version`                            `sys.is_finalizing()`
- `sys.argv`                                   `sys.is_stack_trampoline_active()`
- `sys.audit(`                                 `sys.last_exc`
- `sys.base_exec_prefix`                       `sys.last_traceback`
- `sys.base_prefix`                            `sys.last_type(`
- `sys.breakpointhook(`                        `sys.last_value`
- `sys.builtin_module_names`                   `sys.maxsize`
- `sys.byteorder`                              `sys.maxunicode`
- `sys.call_tracing(`                          `sys.meta_path`
- `sys.copyright`                              `sys.modules`
- `sys.deactivate_stack_trampoline()`          `sys.monitoring`
- `sys.displayhook(`                           `sys.orig_argv`
- `sys.dont_write_bytecode`                    `sys.path`
- `sys.exc_info()`                             `sys.path_hooks`
- `sys.excepthook(`                            `sys.path_importer_cache`
- `sys.exception()`                            `sys.platform`
- `sys.exec_prefix`                            `sys.platlibdir`
- `sys.executable`                             `sys.prefix`
- `sys.exit(`                                  `sys.ps1`
- `sys.flags`                                  `sys.ps2`
- `sys.float_info`                             `sys.pycache_prefix`
- `sys.float_repr_style`                       `sys.set_asyncgen_hooks(`
- `sys.get_asyncgen_hooks()`                   `sys.set_coroutine_origin_tracking_depth(`
- `sys.get_coroutine_origin_tracking_depth()`  `sys.set_int_max_str_digits(`
- `sys.get_int_max_str_digits()`               `sys.setdlopenflags(`
- `sys.getallocatedblocks()`                   `sys.setprofile(`
- `sys.getdefaultencoding()`                   `sys.setrecursionlimit(`
- `sys.getdlopenflags()`                       `sys.setswitchinterval(`
- `sys.getfilesystemencodeerrors()`            `sys.settrace(`
- `sys.getfilesystemencoding()`                `sys.stderr`
- `sys.getprofile()`                         `sys.stdin`
- `sys.getrecursionlimit()`                   `sys.stdlib_module_names`
- `sys.getrefcount(`                          `sys.stdout`
- `sys.getsizeof(`                             `sys.thread_info`
- `sys.getswitchinterval()`                    `sys.unraisablehook(`
- `sys.gettrace()`                        `sys.version`
- `sys.getunicodeinternedsize()`               `sys.version_info`
- `sys.hash_info`                            `sys.warnoptions`
- `sys.hexversion`