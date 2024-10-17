Name:		gelide
Version:	0.1.5
Release:	4
Summary:	Emulators manager
Group:		Emulators
License:	GPLv3
URL:		https://gelide.sourceforge.net/
Source0:	http://sourceforge.net/projects/%{name}/files/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:		gelide-0.1.5-glib.patch
Patch1:		gelide-0.1.5-gcc4.7.patch
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	intltool
BuildRequires:	rarian
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
%patch1 -p1 -b .gcc47~

%build
%configure2_5x
%make

%install
%makeinstall_std

desktop-file-install \
	--remove-key="Version" \
	--remove-key="Encoding" \
	--dir=%{buildroot}%{_datadir}/applications/ \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

rm -rf %{buildroot}/usr/doc

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS ChangeLog README INSTALL COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*.xml
%{_datadir}/%{name}/pixmaps/*
%{_datadir}/%{name}/ui/*
%{_iconsdir}/hicolor/*
%{_mandir}/*/%{name}*


%changelog
* Fri Feb 03 2012 Andrey Bondrov <abondrov@mandriva.org> 0.1.5-2mdv2012.0
+ Revision: 770986
- _desktopdir is not supported by BS, change to _datadir/applications
- imported package gelide


* Fri Jul 22 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 0.1.5-2mib2010.2
- Rebuild for 2010.2
- Little spec clean up
- Fix group
- Fix languages
- Fix .desktop file

* Thu Jul 21 2011 Cristobal Lopez <lopeztobal@gmail.com> 0.1.5-1mib2011.0
- Initial build for Mandriva
