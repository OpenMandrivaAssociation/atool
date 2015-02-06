%define name atool
%define version 0.39.0
%define release 2

Summary:        A script for managing file archives of various types
Name:           %{name}
Group:		Archiving/Compression
Version:        %{version}
Release:        %{release}
Source:         http://savannah.nongnu.org/download/atool/%{name}-%{version}.tar.gz
Patch: atool-0.37.0-bash-completion.patch
URL:            http://www.nongnu.org/atool/
License:        GPLv2+
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
BuildArch:	noarch
Requires:	perl

%description
atool is a script for managing file archives of various types (tar,
tar+gzip, zip, etc). The main command is probably 'aunpack' which
extracts files from an archive. It overcomes the dreaded "multiple
files in archive root" problem by first extracting to a unique
subdirectory, and then moving back the files if possible. aunpack
also prevents local files from being overwritten by mistake. Other
commands provided are apack (for creating archives), als (for listing
files in archives), and acat (for extracting files to stdout). 

%prep
%setup -q
%patch -p1 -b .bash-completion

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
install -m 644 -D extra/bash-completion-atool_0.1-1 %buildroot%_sysconfdir/bash_completion.d/atool

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README ChangeLog NEWS TODO
%config(noreplace) %_sysconfdir/bash_completion.d/atool
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Wed Apr 04 2012 GÃ¶tz Waschk <waschk@mandriva.org> 0.39.0-1
+ Revision: 789114
- update to new version 0.39.0

* Tue Aug 16 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.38.0-1
+ Revision: 694674
- update to new version 0.38.0

* Fri Oct 02 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.37.0-2mdv2011.0
+ Revision: 452468
- add xz to bash-completion file

* Sat Aug 15 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.37.0-1mdv2010.0
+ Revision: 416444
- update to new version 0.37.0

* Wed Aug 05 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.36.0-2mdv2010.0
+ Revision: 410000
- add tbz2 extension to bash completion

* Fri Feb 27 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.36.0-1mdv2009.1
+ Revision: 345827
- update to new version 0.36.0

* Fri Jan 16 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.35.0-3mdv2009.1
+ Revision: 330139
- update patch to include the lzma extension
- update license

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.35.0-2mdv2009.0
+ Revision: 266221
- rebuild early 2009.0 package (before pixel changes)

* Mon Jun 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.35.0-1mdv2009.0
+ Revision: 217016
- new version

* Wed Apr 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.34.0-1mdv2009.0
+ Revision: 192443
- new version
- add bash completion

  + Pascal Terjan <pterjan@mandriva.org>
    - Don't define package macro

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 23 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.33.0-1mdv2008.0
+ Revision: 70652
- new version

* Wed Jul 25 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.32.0-2mdv2008.0
+ Revision: 55218
- Import atool



* Thu Jul 20 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.32.0-1mdv2007.0
- Rebuild

* Wed Dec 14 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.32.0-1mdk
- New release 0.32.0
- use mkrel

* Tue Aug 09 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.31.0-1mdk
- New release 0.31.0

* Mon Jul 25 2005 Götz Waschk <waschk@mandriva.org> 0.30.0-2mdk
- fix URLs

* Mon Jul 25 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.30.0-1mdk
- 0.30.0

* Thu Jul 07 2005 Götz Waschk <waschk@mandriva.org> 0.29.0-2mdk
- Rebuild

* Tue Jul  6 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.29.0-1mdk
- New release 0.29.0

* Fri Jun 18 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.28.0-1mdk
- 0.28.0
- remove patch merged upstream

* Sun Apr 18 2004 Götz Waschk <waschk@linux-mandrake.com> 0.27.0-2mdk
- fix lha

* Fri Nov 14 2003 Götz Waschk <waschk@linux-mandrake.com> 0.27.0-1mdk
- fix build
- new version

* Sat May 24 2003 Götz Waschk <waschk@linux-mandrake.com> 0.26.0-1mdk
- new version

* Fri Dec 27 2002 Götz Waschk <waschk@linux-mandrake.com> 0.25.0-2mdk
- rebuild

* Sat Nov  9 2002 Götz Waschk <waschk@linux-mandrake.com> 0.25.0-1mdk
- new version

* Thu Oct 10 2002 Götz Waschk <waschk@linux-mandrake.com> 0.24.0-1mdk
- use installation macro
- new version

* Tue Oct  1 2002 Götz Waschk <waschk@linux-mandrake.com> 0.23.0-2mdk
- add some man page symlinks for the individual commands

* Mon Sep 30 2002 Götz Waschk <waschk@linux-mandrake.com> 0.23.0-1mdk
- initial Mandrake package
