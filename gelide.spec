Name:		gelide
Version:	0.1.5
Release:	%mkrel 2
Summary:	Emulators manager
Group:		Emulators
License:	GPLv3
URL:		http://gelide.sourceforge.net/
Source0:	http://sourceforge.net/projects/%{name}/files/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:		gelide-0.1.5-glib.patch
BuildRequires:	desktop-file-utils
BuildRequires:	libgtkmm2.4-devel
BuildRequires:	libxml2-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	intltool
BuildRequires:	gcc-c++

%description
Gelide is a configurable frontend which let you manage any kind of emulated
system (PC, console, arcade, etc) letting you to catalog and launch any game
from any existing emulator under GNU/Linux. With Gelide, you can configure
any emulator with command line parameters support, without the need of
remember them every now and then.

%prep
%setup -q
%patch0 -p1 -b .glib~

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}

%makeinstall_std

desktop-file-install \
	--remove-key="Version" \
	--remove-key="Encoding" \
	--dir=%{buildroot}%{_desktopdir} \
	%{buildroot}%{_desktopdir}/%{name}.desktop

%__rm -rf %{buildroot}/usr/doc

%find_lang %{name}

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog README INSTALL COPYING
%{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_datadir}/%{name}/*.xml
%{_datadir}/%{name}/pixmaps/*
%{_datadir}/%{name}/ui/*
%{_datadir}/gnome/help/%{name}/*
%{_iconsdir}/hicolor/*
%{_mandir}/*/%{name}*
%{_datadir}/omf/%{name}/*.omf

