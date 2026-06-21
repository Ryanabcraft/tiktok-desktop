[Setup]
AppName=TikTok Desktop
AppVersion=1.0.0
AppPublisher=Ryanabcraft
AppPublisherURL=https://github.com/Ryanabcraft/tiktok-desktop
AppSupportURL=https://github.com/Ryanabcraft/tiktok-desktop/issues
DefaultDirName={autopf}\TikTok Desktop
DefaultGroupName=TikTok Desktop
UninstallDisplayIcon={app}\TikTok.exe
UninstallDisplayName=TikTok Desktop
OutputDir=dist_installer
OutputBaseFilename=TikTok-Setup
Compression=lzma2
SolidCompression=yes
PrivilegesRequired=admin

[Languages]
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "dist_py\TikTok.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{commondesktop}\TikTok"; Filename: "{app}\TikTok.exe"; WorkingDir: "{app}"; Tasks: desktopicon
Name: "{group}\TikTok Desktop"; Filename: "{app}\TikTok.exe"; WorkingDir: "{app}"
Name: "{group}\Desinstalar TikTok Desktop"; Filename: "{uninstallexe}"

[Tasks]
Name: "desktopicon"; Description: "Criar atalho na &Área de Trabalho"; GroupDescription: "Atalhos:"; Flags: checkedonce

[Run]
Filename: "{app}\TikTok.exe"; Description: "Executar TikTok Desktop"; Flags: postinstall nowait skipifsilent
