Summary:	IDE S.M.A.R.T. test and query tool
Summary(pl):	IDE S.M.A.R.T. - narzêdzie testuj±ce i odpytuj±ce
Name:		ide-smart
Version:	1.3
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://metalab.unc.edu/pub/Linux/hardware/%{name}-%{version}.tar.gz
URL:		http://www.linux-ide.org/smart.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ide-smart performs and queries the results of various non destructive
tests on a SMART capable IDE DEVICE. You must have a BIOS and hardware
that supports it.

%description -l pl
ide-smart wykonuje zapytania i odczytuje rezultaty niedestrukcyjnych
testów na urz±dzeniu IDE obs³uguj±cym SMART. Musisz mieæ BIOS oraz
sprzêt obs³uguj±cy SMART.

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
