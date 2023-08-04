Name:		kaidan
Version:	0.8.0
Release:	4
Summary:	XMPP based messenger for Plasma Mobile
Url:		https://www.kaidan.im
Source0:	https://invent.kde.org/network/kaidan/-/archive/v%{version}/kaidan-v%{version}.tar.bz2
License:	GPLv3
Group:		Applications/Productivity
# (tpg) patches from upstream
Patch0:		https://invent.kde.org/network/kaidan/-/commit/9a2f88779064b46ae097a354c97d657901f47d01.patch
Patch1:		https://invent.kde.org/network/kaidan/-/commit/c92fe3125c08e61b454b41f151b435a6a9e6da4b.patch
Patch2:		https://invent.kde.org/network/kaidan/-/commit/dc41a3f3850308d5204134ae08e66f20a58195f9.patch
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
BuildRequires:	cmake(KF5QQC2DesktopStyle)
Requires:	qt5-qtlocation
Requires:	kirigami

%description
XMPP based messenger for Plasma Mobile.

%prep
%autosetup -p1 -n %{name}-v%{version}
%cmake_kde5 \
	-DQUICK_COMPILER=TRUE \
	-DI18N=TRUE \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/kaidan
%{_datadir}/applications/im.kaidan.kaidan.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/kaidan
%{_datadir}/knotifications5/kaidan.notifyrc
%{_datadir}/metainfo/im.kaidan.kaidan.appdata.xml
