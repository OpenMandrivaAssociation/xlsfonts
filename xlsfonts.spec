Name:		xlsfonts
Version:	1.0.8
Release:	1
Summary:	Server font list displayer for X
Group:		Development/X11
License:	MIT
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(x11)
BuildRequires:	x11-util-macros

%description
Xlsfonts lists the fonts that match the given pattern. The wildcard character
"*" may be used to match any sequence of characters (including none), and "?"
to match any single character.

%prep
%autosetup -p1

%build
%configure \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/xlsfonts
%doc %{_mandir}/man1/xlsfonts.1*
