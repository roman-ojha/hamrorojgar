import React, { memo, useEffect, useMemo, useState } from "react";
import styles from "@/styles/pages/jobs.module.scss";
import { Icon } from "@iconify/react";
import { useRouter } from "next/router";
import { api } from "@/services/api";
import { isOkResponse } from "@/utils/checkApiStatus";
import { useAppState } from "@/hooks/useAppState";

const SearchJobs = (): React.JSX.Element => {
  const [{ storeJobs }] = useAppState([]);
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
  }, [router]);

  useEffect(() => {
    const fetchJobs = async () => {
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
    fetchJobs();
  }, [queries, storeJobs]);

  return (
    <>
      <form className={styles.jobs__search}>
        <div className={styles.jobs__search__what}>
          <label htmlFor="search_what">What</label>
          <div className={styles.jobs__search__what__input_field}>
            <input
              type="search"
              name="search_what"
              id="search_what"
              placeholder="Search..."
            />
            <Icon
              className={styles.jobs__search__what__input_field__icon}
              icon="ic:outline-search"
            />
          </div>
        </div>
        <div className={styles.jobs__search__where}>
          <label htmlFor="district">Where</label>
          <select name="district" id="district">
            <option value="">District</option>
            <option value="">jhapa</option>
          </select>
          <select name="municipality" id="municipality">
            <option value="">Municipality</option>
            <option value="">kamal</option>
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
