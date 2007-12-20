%define name acpitool
%define version 0.4.7
%define release %mkrel 1

Summary: A Linux ACPI client 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://freeunix.dyndns.org:8088/ftp_site/pub/unix/acpitool/%name-%version.tar.bz2
License: GPL 
Group: System/Kernel and hardware
Url: http://freeunix.dyndns.org:8088/site2/acpitool.shtml
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
It's a small command-line application,
intended to be a replacement for the apm tool.

%prep
%setup -q

%build
%configure2_5x

perl -pi -e "s|/usr/local|$RPM_BUILD_ROOT/usr|g" Makefile
perl -pi -e "s|man/man1|share/man/man1|g" Makefile

%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/acpitool
%{_mandir}/man1/acpitool*


