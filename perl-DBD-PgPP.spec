# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	PgPP
Summary:	A PostgresSQL interface for Perl
Summary(cs):	PostgresSQL rozhraní pro Perl
Summary(da):	Et PostgreSQL-grænseflade for Perl
Summary(de):	Ein PostgreSQL-Interface für Perl
Summary(es):	Interfaz PostgresSQL para Perl
Summary(fr):	Interface PostgresSQL pour Perl
Summary(it):	Interfaccia PostgreSQL per Perl
Summary(ja):	Perl ¤Î PostgreSQL ¥¤¥ó¥¿¡¼¥Õ¥§¥¤¥¹
Summary(ko):	ÆŞÀ» À§ÇÑ PostgresSQL ÀÎÅÍÆäÀÌ½º
Summary(nb):	Et PostgreSQL-grensesnitt for Perl
Summary(pl):	Perlowy interfejs do PostgresSQLa
Summary(pt):	Uma interface de Perl para o PostgresSQL
Summary(pt_BR):	Uma interface de Perl para o PostgresSQL
Summary(ru):	éÎÔÅÒÆÅÊÓ PostgresSQL ÄÌÑ Perl
Summary(sv):	Ett gränssnitt till PostgresSQL för Perl
Summary(uk):	Perl-¦ÎÔÅÒÆÅÊÓ ÄÏ PostgresSQL
Summary(zh_CN):	Perl µÄ PostgresSQL ½çÃæ¡£
Name:		perl-DBD-PgPP
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	159d54a21eda08ab93fd44f2791cf56f
BuildRequires:	perl-DBI
BuildRequires:	perl-devel >= 5.6
BuildRequires:	postgresql-devel
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#define		_noautoreq 'perl(POSIX(qw(isprint)))'

%description
DBD::PgPP - PostgreSQL database driver for the DBI module.

%description -l cs
Implementace DBI pro PostgreSQL do Perlu.

%description -l da
Denne pakke indeholder en implementation af DBI for PostgreSQL for
Perl.

%description -l de
Dieses Paket enthält eine Implementierung von PostgreSQL für Perl.

%description -l es
Este paquete contiene una implementación de DBI para PotgreSQL para
PERL.

%description -l fr
Ce paquetage contient une mise en oeuvre de DBI pour PostgreSQL pour
Perl.

%description -l it
Questo pacchetto contiene un'implementazione di DBI per PostgreSQL per
Perl.

%description -l ja
¤³¤Î¥Ñ¥Ã¥±¡¼¥¸¤Ë¤Ï Perl ¤Î PostgreSQL ÍÑ DBI ¼ÂÁõ¤¬¼ıÏ¿¤µ¤ì¤Æ¤¤¤Ş¤¹¡£

%description -l ko
ÀÌ ÆĞÅ°Áö´Â ÆŞÀ» À§ÇÑ PostgreSQLÀÇ DBI ½ÇÇöÀ» Æ÷ÇÔÇÏ°í ÀÖ½À´Ï´Ù.

%description -l nb
Denne pakken inneholder en implementasjon av DBI for PostgreSQL for
Perl.

%description -l pl
DBD::PgPP - Sterownik bazy danych PostgreSQL dla modu³u DBI.

%description -l pt
Este pacote contém uma implementação de DBI para o PostgreSQL para o
Perl.

%description -l pt_BR
Este pacote contém uma implementação de DBI para o PostgreSQL para o
Perl.

%description -l ru
üÔÏ ĞÁËÅÔ ÓÏÄÅÒÖÉÔ ÒÅÁÌÉÚÁÃÉÀ DBI ÄÌÑ PostgreSQL ÄÌÑ Perl.

%description -l sv
Detta paket innehåller en implementation av DBI för PostgreSQL för
Perl.

%description -l zh_CN
¸ÃÈí¼ş°ü°üÀ¨ÓÃÓÚ Perl µÄ PostgreSQL µÄ DBI ÊµÏÖ¡£

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
POSTGRES_LIB="%{_libdir}"; export POSTGRES_LIB
POSTGRES_INCLUDE="%{_includedir}/postgresql"; export POSTGRES_INCLUDE
%{__perl} Makefile.PL 
%{__make} \
	OPTIMIZE="%{rpmcflags}"

# Needed to be set for tests:
#PG_TEST_DB=<database>
#PG_TEST_USER=<user>
#PG_TEST_PASS=<password>
#PG_TEST_HOST=<hostname>*
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/%{pdir}/*
%dir %{perl_sitearch}/auto/DBD/PgPP
%{_mandir}/man[13]/*
