Summary:	IDE S.M.A.R.T. test and query tool
Summary(pl.UTF-8):	IDE S.M.A.R.T. - narzędzie testujące i odpytujące
Name:		ide-smart
Version:	1.4
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://lightside.eresmas.com/%{name}-%{version}.tar.gz
# Source0-md5:	268fb2a29224b4554073edaad50b9cb0
URL:		http://www.linux-ide.org/smart.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ide-smart performs and queries the results of various non destructive
tests on a SMART capable IDE DEVICE. You must have a BIOS and hardware
that supports it.

%description -l pl.UTF-8
ide-smart wykonuje zapytania i odczytuje rezultaty niedestrukcyjnych
testów na urządzeniu IDE obsługującym SMART. Musisz mieć BIOS oraz
sprzęt obsługujący SMART.

%prep
%setup -q

%build
%{__make} clean
%{__make} CC="%{__cc}" PROF="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install ide-smart $RPM_BUILD_ROOT%{_sbindir}
install ide-smart.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
