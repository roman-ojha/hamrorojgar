import React, { memo, useEffect, useMemo, useState } from "react";
import styles from "@/styles/pages/jobs.module.scss";
import { Icon } from "@iconify/react";
import { useRouter } from "next/router";

const SearchJobs = (): React.JSX.Element => {
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
    if (router.query["q"] && !Array.isArray(router.query["q"])) {
      if (
        router.query["district"] &&
        !Array.isArray(router.query["district"])
      ) {
        if (
          router.query["municipality"] &&
          !Array.isArray(router.query["municipality"])
        ) {
          setQueries({
            q: router.query["q"],
            district: router.query["district"],
            municipality: router.query["municipality"],
          });
        } else {
          setQueries({
            q: router.query["q"],
            district: router.query["district"],
            municipality: null,
          });
        }
      } else {
        setQueries({
          q: router.query["q"],
          district: null,
          municipality: null,
        });
      }
    }
  }, [router]);

  useEffect(() => {
    console.log(queries);
    if (queries.q) {
      if (queries.municipality && queries.district) {
      }
    }
  }, [queries]);

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
