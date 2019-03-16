#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mitools
Version  : 2.3
Release  : 4
URL      : https://cran.r-project.org/src/contrib/mitools_2.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mitools_2.3.tar.gz
Summary  : Tools for multiple imputation of missing data
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : clr-R-helpers

%description
multiple-imputation datasets.

%prep
%setup -q -c -n mitools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1531191782

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1531191782
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mitools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mitools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mitools
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library mitools|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mitools/DESCRIPTION
/usr/lib64/R/library/mitools/INDEX
/usr/lib64/R/library/mitools/Meta/Rd.rds
/usr/lib64/R/library/mitools/Meta/data.rds
/usr/lib64/R/library/mitools/Meta/demo.rds
/usr/lib64/R/library/mitools/Meta/features.rds
/usr/lib64/R/library/mitools/Meta/hsearch.rds
/usr/lib64/R/library/mitools/Meta/links.rds
/usr/lib64/R/library/mitools/Meta/nsInfo.rds
/usr/lib64/R/library/mitools/Meta/package.rds
/usr/lib64/R/library/mitools/Meta/vignette.rds
/usr/lib64/R/library/mitools/NAMESPACE
/usr/lib64/R/library/mitools/NEWS
/usr/lib64/R/library/mitools/R/mitools
/usr/lib64/R/library/mitools/R/mitools.rdb
/usr/lib64/R/library/mitools/R/mitools.rdx
/usr/lib64/R/library/mitools/data/smi.rda
/usr/lib64/R/library/mitools/demo/mi.R
/usr/lib64/R/library/mitools/doc/index.html
/usr/lib64/R/library/mitools/doc/smi.R
/usr/lib64/R/library/mitools/doc/smi.Rnw
/usr/lib64/R/library/mitools/doc/smi.pdf
/usr/lib64/R/library/mitools/dta/smif1.dta
/usr/lib64/R/library/mitools/dta/smif2.dta
/usr/lib64/R/library/mitools/dta/smif3.dta
/usr/lib64/R/library/mitools/dta/smif4.dta
/usr/lib64/R/library/mitools/dta/smif5.dta
/usr/lib64/R/library/mitools/dta/smim1.dta
/usr/lib64/R/library/mitools/dta/smim2.dta
/usr/lib64/R/library/mitools/dta/smim3.dta
/usr/lib64/R/library/mitools/dta/smim4.dta
/usr/lib64/R/library/mitools/dta/smim5.dta
/usr/lib64/R/library/mitools/help/AnIndex
/usr/lib64/R/library/mitools/help/aliases.rds
/usr/lib64/R/library/mitools/help/mitools.rdb
/usr/lib64/R/library/mitools/help/mitools.rdx
/usr/lib64/R/library/mitools/help/paths.rds
/usr/lib64/R/library/mitools/html/00Index.html
/usr/lib64/R/library/mitools/html/R.css
