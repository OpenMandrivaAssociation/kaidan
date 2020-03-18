%define snapshot 20200312
%define commit 0c006512dfc0312c3f8d8c688657d875f2085cc2

Name:		kaidan
Version:	0.0
Release:	0.%{snapshot}.1
Summary:	XMPP based messenger for Plasma Mobile
Source0:	https://invent.kde.org/kde/kaidan/-/archive/master/kaidan-%{snapshot}.tar.bz2
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
%autosetup -p1 -n %{name}-master-%{commit}
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

