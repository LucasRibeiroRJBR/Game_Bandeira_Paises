# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\lucas.ribeiro\\Downloads\\Github\\Game_Bandeira_Paises\\app.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\lucas.ribeiro\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\customtkinter', 'customtkinter/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Duda Flags',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\lucas.ribeiro\\Downloads\\Github\\Game_Bandeira_Paises\\duda_flags.ico'],
)
