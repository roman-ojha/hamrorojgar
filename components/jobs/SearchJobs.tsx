import React, { memo, useEffect, useState } from "react";
import styles from "@/styles/pages/jobs.module.scss";
import { Icon } from "@iconify/react";
import { useRouter } from "next/router";
import { api } from "@/services/api";
import { isOkResponse } from "@/utils/checkApiStatus";
import { useAppState } from "@/hooks/useAppState";

const SearchJobs = (): React.JSX.Element => {
  const [{ storeJobs, fetchJobs }] = useAppState([]);
  const [districts, setDistricts] = useState<{ id: number; name: string }[]>(
    []
  );
  const [municipalities, setMunicipalities] = useState<
    { id: number; name: string; get_type_label: string }[]
  >([]);
  const router = useRouter();
  //   console.log(router.query);
  const [queries, setQueries] = useState<{
    q: string | null;
    district: string | null;
    municipality: string | null;
  }>({
    q: null,
    district: null,
    municipality: null,
  });

  useEffect(() => {
    setQueries({
      q:
        router.query["q"] && !Array.isArray(router.query["q"])
          ? router.query["q"]
          : null,
      district:
        router.query["district"] && !Array.isArray(router.query["district"])
          ? router.query["district"]
          : null,
      municipality:
        router.query["municipality"] &&
        !Array.isArray(router.query["municipality"])
          ? router.query["municipality"]
          : null,
    });
    if (
      !router.query["q"] &&
      !router.query["district"] &&
      !router.query["municipality"] &&
      router.isReady
    ) {
      fetchJobs();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [router]);

  useEffect(() => {
    const fetchAndStoreJobs = async () => {
      if (queries.q || queries.district || queries.municipality) {
        const resJobs = await api.jobs.search(
          queries.q ? queries.q : "",
          queries.district ? queries.district : "",
          queries.municipality ? queries.municipality : ""
        );
        if (resJobs && isOkResponse(resJobs?.status)) {
          storeJobs(resJobs.data);
        }
      }
    };
    fetchAndStoreJobs();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [queries]);

  const handleWhatSearch = (e: React.ChangeEvent<HTMLInputElement>) => {
    const search = (data: string) => {
      setQueries({
        ...queries,
        q: data,
      });
      const url = new URL(window.location.href);
      url.searchParams.set("q", data);
      url.searchParams.set(
        "district",
        queries.district ? queries.district : ""
      );
      url.searchParams.set(
        "municipality",
        queries.municipality ? queries.municipality : ""
      );
      window.history.replaceState({}, "", url.toString());
    };
    search(e.target.value);
  };

  const handleDistrictSearch = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setQueries({
      ...queries,
      district: e.target.value,
    });
    const url = new URL(window.location.href);
    url.searchParams.set("q", queries.q ? queries.q : "");
    url.searchParams.set("district", e.target.value);
    url.searchParams.set(
      "municipality",
      queries.municipality ? queries.municipality : ""
    );
    window.history.replaceState({}, "", url.toString());
  };

  const handleMunicipalitySearch = (
    e: React.ChangeEvent<HTMLSelectElement>
  ) => {
    setQueries({
      ...queries,
      municipality: e.target.value,
    });
    const url = new URL(window.location.href);
    url.searchParams.set("q", queries.q ? queries.q : "");
    url.searchParams.set("district", queries.district ? queries.district : "");
    url.searchParams.set("municipality", e.target.value);
    window.history.replaceState({}, "", url.toString());
  };

  const getDistricts = async () => {
    const res = await api.district.get();
    if (res && isOkResponse(res.status)) {
      setDistricts(res.data);
    }
  };

  const fetchMunicipalities = async (
    e: React.ChangeEvent<HTMLSelectElement>
  ) => {
    const district_id = e.target.selectedOptions[0].getAttribute("data-key");
    const res = await api.municipality.get(district_id as string);
    if (res && isOkResponse(res.status)) {
      // console.log(res.data);
      setMunicipalities(res.data);
    }
  };

  useEffect(() => {
    getDistricts();
  }, []);

  return (
    <>
      <form
        className={styles.jobs__search}
        onSubmit={(e) => {
          e.preventDefault();
        }}
      >
        <div className={styles.jobs__search__what}>
          <label htmlFor="search_what">What</label>
          <div className={styles.jobs__search__what__input_field}>
            <input
              type="search"
              name="q"
              id="search_what"
              placeholder="Search..."
              onChange={handleWhatSearch}
            />
            <Icon
              className={styles.jobs__search__what__input_field__icon}
              icon="ic:outline-search"
            />
          </div>
        </div>
        <div className={styles.jobs__search__where}>
          <label htmlFor="district">Where</label>
          <select
            name="district"
            id="district"
            onChange={(e) => {
              handleDistrictSearch(e);
              fetchMunicipalities(e);
            }}
          >
            <option value="">District</option>
            {districts.map((district) => (
              <option
                key={district.id}
                value={district.name}
                data-key={district.id}
              >
                {district.name}
              </option>
            ))}
          </select>
          <select
            name="municipality"
            id="municipality"
            onChange={handleMunicipalitySearch}
          >
            <option value="">Municipality</option>
            {municipalities.map((municipality) => (
              <option key={municipality.id} value={municipality.name}>
                {municipality.name}
              </option>
            ))}
          </select>
          <Icon
            className={styles.jobs__search__where__icon}
            icon="ic:outline-search"
          />
        </div>
        <div className={styles.jobs__search__where}></div>
      </form>
    </>
  );
};

export default memo(SearchJobs);
