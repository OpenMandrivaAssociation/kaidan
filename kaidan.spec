Name:		kaidan
Version:	0.5.0
Release:	1
Summary:	XMPP based messenger for Plasma Mobile
Url:      https://www.kaidan.im
Source0:  https://download.kde.org/stable/kaidan/%{version}/%{name}-%{version}.tar.xz
# Mirror
#Source0:	https://invent.kde.org/kde/kaidan/-/archive/master/kaidan-%{version}.tar.xz
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	cmake(Qt5Positioning)
BuildRequires:	cmake(Qt5Location)
BuildRequires:	qt5-qtlocation
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(Qt5QuickCompiler)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(PkgConfig)
BuildRequires:	cmake(Perl)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(QXmpp)
BuildRequires:	cmake(ZXing)

%description
XMPP based messenger for Plasma Mobile

%prep
%autosetup -p1 -n %{name}-%{version}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/kaidan
%{_datadir}/applications/kaidan.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/kaidan
%{_datadir}/knotifications5/kaidan.notifyrc
%{_datadir}/metainfo/im.kaidan.kaidan.appdata.xml
