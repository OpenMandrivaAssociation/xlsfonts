Name:		xlsfonts
Version:	1.0.4
Release:	7
Summary:	Server font list displayer for X
Group:		Development/X11
License:	MIT
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11)
BuildRequires:	x11-util-macros
Patch0:		xlsfonts-aarch64.patch

%description
Xlsfonts lists the fonts that match the given pattern. The wildcard character
"*" may be used to match any sequence of characters (including none), and "?"
to match any single character.

%prep
%setup -q
%apply_patches

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/xlsfonts
%{_mandir}/man1/xlsfonts.1*

