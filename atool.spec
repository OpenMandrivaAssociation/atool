Summary:        A script for managing file archives of various types
Name:           atool
Group:		Archiving/Compression
Version:        0.39.0
Release:        2
Source:         http://savannah.nongnu.org/download/atool/%{name}-%{version}.tar.gz
Patch: atool-0.37.0-bash-completion.patch
URL:            https://www.nongnu.org/atool/
License:        GPLv2+
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
%makeinstall
install -m 644 -D extra/bash-completion-atool_0.1-1 %{buildroot}%{_sysconfdir}/bash_completion.d/atool

%clean

%files
%doc README ChangeLog NEWS TODO
%config(noreplace) %{_sysconfdir}/bash_completion.d/atool
%{_bindir}/*
%{_mandir}/man1/*


