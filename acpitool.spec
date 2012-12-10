%define name acpitool
%define version 0.5.1
%define release %mkrel 2

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
%setup -q -n %name-%{version}

%build
%configure2_5x

perl -pi -e "s|/usr/local|$RPM_BUILD_ROOT/usr|g" Makefile
perl -pi -e "s|man/man1|share/man/man1|g" Makefile

make

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




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-2mdv2011.0
+ Revision: 616500
- the mass rebuild of 2010.0 packages

* Fri Aug 14 2009 Frederik Himpe <fhimpe@mandriva.org> 0.5.1-1mdv2010.0
+ Revision: 416372
- Update to new version 0.5.1
- Remove string patch integrated upstream

* Thu Mar 05 2009 Antoine Ginies <aginies@mandriva.com> 0.5.0-1mdv2009.1
+ Revision: 348867
- fix patch0 decleration

* Thu Jul 24 2008 Erwan Velu <erwan@mandriva.org> 0.5.0-1mdv2009.0
+ Revision: 245873
- 0.5.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.4.7-1mdv2008.1
+ Revision: 135817
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Feb 07 2007 Lenny Cartier <lenny@mandriva.com> 0.4.7-1mdv2007.0
+ Revision: 117187
- Update to 0.4.7
- Import acpitool

* Tue Sep 05 2006 Jerome Soyer <saispo@mandriva.org> 0.4.6-1mdv2007.0
- New release 0.4.6

* Wed Jun 28 2006 Lenny Cartier <lenny@mandriva.com> 0.4.5-2mdv2007.0
- rebuild

* Tue May 16 2006 Lenny Cartier <lenny@mandriva.com> 0.4.5-1mdk
- 0.4.5

* Mon Feb 06 2006 Lenny Cartier <lenny@mandriva.com> 0.4.4-1mdk
- 0.4.4

* Mon Dec 12 2005 Erwan Velu <erwan@seanodes.com> 0.4.0-1mdk
- 0.4.0

* Tue Apr 19 2005 Giuseppe Ghibò <ghibo@mandrakesoft.com> 0.2.7-1mdk
- 0.2.7.

* Tue Sep 14 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.2.5-1mdk
- 0.2.5

* Wed Jul 14 2004 Erwan Velu <erwan@mandrakesoft.com> 0.2-1mdk
- Initial mdk package

