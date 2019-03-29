Summary:	Userspace RCU implementation
Summary(pl.UTF-8):	Implementacja RCU w przestrzeni użytkownika
Name:		userspace-rcu
Version:	0.10.2
Release:	1
License:	LGPL v2.1+ (library), GPL v2 (tests)
Group:		Libraries
Source0:	https://lttng.org/files/urcu/%{name}-%{version}.tar.bz2
# Source0-md5:	7c424c5183ec009d87e0f70c23e92f1b
URL:		http://liburcu.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
liburcu is a LGPL userspace RCU (read-copy-update) library. This data
synchronization library provides read-side access which scales
linearly with the number of cores. It does so by allowing multiples
copies of a given data structure to live at the same time, and by
monitoring the data structure accesses to detect grace periods after
which memory reclamation is possible.

liburcu-cds provides efficient data structures based on RCU and
lock-free algorithms. Those structures include hash tables, queues,
stacks, and doubly-linked lists.

%description -l pl.UTF-8
liburcu to dostępna na licencji LGPL biblioteka będąca implementacją
algorytmu RCU (read-copy-update) w przestrzeni użytkownika. Ta
biblioteka synchronizacji danych pozwala na dostęp w trybie odczytu
skalujący się liniowo wraz z liczbą rdzeni. Jest to osiągalne poprzez
zezwolenie na istnienie naraz wielu kopii struktur danych i śledzenie
dostępów do tych struktur, aby wykryć okresy, kiedy możliwe jest
odzyskanie pamięci.

liburdu-cms udostępnia wydajne struktury danych oparte na algorytmach
RCU oraz bez blokad. Struktury te obejmują tablice haszujące, kolejki,
stosy i listy dwukierunkowe.

%package devel
Summary:	Header files for Userspace RCU libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek Userspace RCU
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Userspace RCU libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Userspace RCU.

%package static
Summary:	Static Userspace RCU libraries
Summary(pl.UTF-8):	Statyczne biblioteki Userspace RCU
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Userspace RCU libraries.

%description static -l pl.UTF-8
Statyczne biblioteki Userspace RCU.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# *.la kept - urcu-common not handled in any way in .pc files

# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/userspace-rcu/{{rcu,cds,uatomic}-api.md,LICENSE,README.md,solaris-build.md}

install -d $RPM_BUILD_ROOT%{_examplesdir}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/userspace-rcu/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README.md lgpl-relicensing.txt
%attr(755,root,root) %{_libdir}/liburcu.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liburcu.so.6
%attr(755,root,root) %{_libdir}/liburcu-bp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liburcu-bp.so.6
%attr(755,root,root) %{_libdir}/liburcu-cds.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liburcu-cds.so.6
%attr(755,root,root) %{_libdir}/liburcu-common.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liburcu-common.so.6
%attr(755,root,root) %{_libdir}/liburcu-mb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liburcu-mb.so.6
%attr(755,root,root) %{_libdir}/liburcu-qsbr.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liburcu-qsbr.so.6
%attr(755,root,root) %{_libdir}/liburcu-signal.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liburcu-signal.so.6

%files devel
%defattr(644,root,root,755)
%doc doc/{rcu,cds,uatomic}-api.md
%attr(755,root,root) %{_libdir}/liburcu.so
%attr(755,root,root) %{_libdir}/liburcu-bp.so
%attr(755,root,root) %{_libdir}/liburcu-cds.so
%attr(755,root,root) %{_libdir}/liburcu-common.so
%attr(755,root,root) %{_libdir}/liburcu-mb.so
%attr(755,root,root) %{_libdir}/liburcu-qsbr.so
%attr(755,root,root) %{_libdir}/liburcu-signal.so
%{_libdir}/liburcu.la
%{_libdir}/liburcu-bp.la
%{_libdir}/liburcu-cds.la
%{_libdir}/liburcu-common.la
%{_libdir}/liburcu-mb.la
%{_libdir}/liburcu-qsbr.la
%{_libdir}/liburcu-signal.la
%{_includedir}/urcu
%{_includedir}/urcu*.h
%{_pkgconfigdir}/liburcu.pc
%{_pkgconfigdir}/liburcu-bp.pc
%{_pkgconfigdir}/liburcu-cds.pc
%{_pkgconfigdir}/liburcu-mb.pc
%{_pkgconfigdir}/liburcu-qsbr.pc
%{_pkgconfigdir}/liburcu-signal.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/liburcu.a
%{_libdir}/liburcu-bp.a
%{_libdir}/liburcu-cds.a
%{_libdir}/liburcu-common.a
%{_libdir}/liburcu-mb.a
%{_libdir}/liburcu-qsbr.a
%{_libdir}/liburcu-signal.a
