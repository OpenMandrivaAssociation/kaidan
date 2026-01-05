Name:		kaidan
Version:	0.14.0
Release:	1
Summary:	XMPP based messenger for Plasma Mobile
Url:		https://www.kaidan.im
Source0:	https://invent.kde.org/network/kaidan/-/archive/v%{version}/kaidan-v%{version}.tar.bz2
License:	GPLv3
Group:		Applications/Productivity

BuildSystem:	cmake
BuildOption:	-DQUICK_COMPILER=TRUE
BuildOption:	-DI18N=TRUE
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6Positioning)
BuildRequires:	cmake(Qt6Location)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KQuickImageEditor)
BuildRequires:	cmake(KF6Prison)
BuildRequires:	cmake(KF6Kirigami)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(PkgConfig)
BuildRequires:	cmake(Perl)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(QXmppQt6)
BuildRequires:	cmake(QXmppOmemoQt6)
BuildRequires:	cmake(ZXing)
BuildRequires:	cmake(KF6QQC2DesktopStyle)
BuildRequires:	cmake(KDSingleApplication-qt6)
BuildRequires:	gomp-devel
Requires:	kirigami

%description
XMPP based messenger for Plasma Mobile.

%conf -p
# FIXME something in the build system seems to force clang
# to use libc++, causing symbol clashes with libstdc++ used by Qt
# For now, simply use a compiler that can't use libc++
export CC=gcc
export CXX=g++

%files -f %{name}.lang
%{_bindir}/kaidan
%{_datadir}/applications/im.kaidan.kaidan.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/kaidan
%{_datadir}/metainfo/im.kaidan.kaidan.appdata.xml
%{_datadir}/knotifications6/kaidan.notifyrc
%{_datadir}/qlogging-categories6/kaidan.categories
