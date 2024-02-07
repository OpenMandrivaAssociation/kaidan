Name:		kaidan
Version:	0.9.1
Release:	1
Summary:	XMPP based messenger for Plasma Mobile
Url:		https://www.kaidan.im
Source0:	https://invent.kde.org/network/kaidan/-/archive/v%{version}/kaidan-v%{version}.tar.bz2
License:	GPLv3
Group:		Applications/Productivity

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
BuildRequires:	cmake(KF5KIO)
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
