Summary: A Linux ACPI client 
Name: acpitool
Version: 0.5.2
Release: 1
Source0: acpitool-0.5.2.tar.xz
License: GPL 
Group: System/Kernel and hardware
Url: https://pagure.io/acpitool

%description
It's a small command-line application,
intended to be a replacement for the apm tool.

%prep
%autosetup -p1
%configure

perl -pi -e "s|/usr/local|$RPM_BUILD_ROOT/usr|g" Makefile
perl -pi -e "s|man/man1|share/man/man1|g" Makefile

%build
%make_build

%install
%make_install

%files
%defattr(-,root,root)
%{_bindir}/acpitool
%{_mandir}/man1/acpitool*
