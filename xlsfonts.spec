Name: xlsfonts
Version: 1.0.2
Release: %mkrel 3
Summary: Server font list displayer for X
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
Xlsfonts lists the fonts that match the given pattern. The wildcard character
"*" may be used to match any sequence of characters (including none), and "?"
to match any single character.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xlsfonts
%{_mandir}/man1/xlsfonts.1*
